import logging
import numpy as np
import pyrosetta

from . import geometry
from . import util
from .chemical.util import functional_groups, resolve_rays
from .dtable import Table

from rif.geom.ray_hash import RayToRay4dHash
from rif.hash import XformHash_bt24_BCC6_X3f

from pyrosetta.rosetta.core.conformation import ResidueFactory

logging.basicConfig(level=logging.WARN)
_logging_handler = "interactive"

# WARN(onalant): constants recommended by Will Sheffler; do not change unless /absolutely/ sure
LEVER = 10
BOUND = 1000
MODE = "fa_standard"

def _init_pyrosetta():
    """Load PyRosetta with the necessary parameter files"""

    from os import path

    _dir = path.join(path.dirname(__file__), "data", "functional_groups")

    param_files = [path.join(_dir, x.resName + ".params") for x in functional_groups.values()]
    opts = [
        "-corrections:beta_nov16",
        "-ignore_waters false",
        "-mute core",
        "-extra_res_fa %s" % (" ".join(param_files)),
        # "-constant_seed",
        "-output_virtual"
    ]

    pyrosetta.init(extra_options=" ".join(opts), set_logging_handler=_logging_handler)

class PrivilegedResidues:

    def __init__(self, path = "/home/onalant/dump/2018-09-11_PRBidentates/*.zarr"):
        """
        Parameters
        ----------
        path : str, optional
            Glob expression to a set of zarr stores.
        """

        self._table = Table.from_multifile(path)

    def match(self, ray1, ray2, group):
        """Construct all of the matched structures for a given ray pair
        and group.

        Parameters
        ----------
        ray1 : np.ndarray
        ray2 : np.ndarray
            Rays used to search in the underlying database.
        group : str
            Dataset to search in.

        Yields
        ------
        pyrosetta.Pose
            Functional group as placed by transform from table.
        """

        dummy_pose = pyrosetta.pose_from_sequence("A", "fa_standard")
        res_type_set = dummy_pose.conformation().residue_type_set_for_conf()

        attrs = self._table.attrs[group]
        cart_resl = attrs["cart_resl"]
        ori_resl = attrs["ori_resl"]
        cart_bound = attrs["cart_bound"]

        lattice = XformHash_bt24_BCC6_X3f(cart_resl, ori_resl, cart_bound)
        raygrid = RayToRay4dHash(ori_resl, LEVER, bound=BOUND)

        hashed_rays = raygrid.get_keys(*(util.numpy_to_rif(r) for r in [ray1, ray2])).item()

        results = self._table.fetch(**{ group: { "hash": hashed_rays } }).compute()
        try:
            ray_frame = geometry.rays_to_transform(ray1, ray2)
        # NOTE(onalant): degenerate case
        except: # pragma: no cover
            return []

        for pos_info in results:
            try:
                stored_frame = lattice.get_center([pos_info["transform"]])["raw"].squeeze()
            # NOTE(onalant): degenerate case
            except: # pragma: no cover
                continue

            resname = pos_info["residue"].decode("utf-8")
            pos_grp = functional_groups[resname]

            dummy_pose.replace_residue(1, ResidueFactory.create_residue(res_type_set.name_map(resname)), False)

            coords = [np.array([*dummy_pose.residues[1].xyz(atom)]) for atom in pos_grp.atoms]
            c = np.stack(coords)

            try:
                pos_frame = geometry.coords_to_transform(c)
            # NOTE(onalant): degenerate case
            except: # pragma: no cover
                continue

            final = ray_frame @ stored_frame @ np.linalg.inv(pos_frame)
            dummy_pose.apply_transform(final)

            yield (hashed_rays, dummy_pose.clone())

    # NOTE(onalant): bring your own residue selector
    def search(self, pose, selector, groups=["all"]):
        """Search for privileged interactions in a pose.

        Parameters
        ----------
        pose : pyrosetta.Pose
            Target structure.
        groups : list of str
            Datasets or groups to search for matches in.
        selector : pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
            Residue selector to apply to the pose.

        Yields
        ------
        tuple of np.uint64, pyrosetta.Pose
            Target ray pair hash and output pose.
        """

        ray_sources = resolve_rays(groups)

        for ray_source in ray_sources:
            for (r1, r2) in ray_source[1](pose, selector):
                yield from self.match(r1, r2, ray_source[0])

_init_pyrosetta()


import multiprocessing
import numpy as np
import pyrosetta
import re

from itertools import permutations

from rif.eigen_types import X3
from rif.geom.ray_hash import RayToRay4dHash
from rif.hash import XformHash_bt24_BCC6_X3f

# NOTE(onalant): change below to desired ray pair provider
from privileged_residues.chemical import catpi
from privileged_residues.geometry import coords_to_transform
from privileged_residues.util import models_from_pdb, numpy_to_rif

dt = [("hash", "u8"), ("residue", "S3"), ("transform", "u8")]

attr = [("cart_resl", 0.1),
        ("ori_resl", 2.0),
        ("cart_bound", 16.0)]
attr = dict(attr)

cart_resl = attr["cart_resl"]
ori_resl = attr["ori_resl"]
cart_bound = attr["cart_bound"]

select = pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()
lattice = XformHash_bt24_BCC6_X3f(cart_resl, ori_resl, cart_bound)
# WARN(onalant): constants recommended by Will Sheffler; do not change unless /absolutely/ sure
LEVER = 10
BOUND = 1000
raygrid = RayToRay4dHash(ori_resl, LEVER, bound=BOUND)

# NOTE(onalant): change as necessary
target_pair = (2, 5)
assert(2 == len(target_pair))

def write_records_from_structure(pipe, posefile):
    print("[WORKER-%s]" % (re.match(".*(\d+)", multiprocessing.current_process().name).group(1)), posefile)
    for pose in models_from_pdb(posefile):
        for (a, b) in permutations(target_pair):
            raypair = catpi.rays_from_residue(pose.residue(a))
            hashed_rays = raygrid.get_keys(*(numpy_to_rif(r) for r in raypair)).item()

            fxA = catpi.rsd_to_fxnl_grp[pose.residue(a).name3()]
            fxB = catpi.rsd_to_fxnl_grp[pose.residue(b).name3()]

            xyzA = np.array([pose.residue(a).xyz(atom) for atom in fxA.atoms])
            xyzB = np.array([pose.residue(b).xyz(atom) for atom in fxB.atoms])

            xfA = coords_to_transform(xyzA)
            xfB = coords_to_transform(xyzB)
            xfrel = xfB @ np.linalg.inv(xfA)

            transform = lattice.get_key(xfrel.astype("f4").flatten().view(X3)).item()

            record = np.array([(hashed_rays, fxB.grp, transform)], dtype=dt)

            pipe.put(record)


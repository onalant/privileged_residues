import numpy as np

from .util import ResInfo
from ..geometry import create_ray

rsd_to_fxnl_grp = {
    # NOTE(onalant): cation
    "ARG": ResInfo("G__", ["CZ", "NH1", "NH2"]),
    "HIS": ResInfo("I__", ["ND1", "CD2", "NE2"]),
    "LYS": ResInfo("A__", ["NZ", "1HZ", "2HZ"]),
    # NOTE(onalant): pi
    "TRP": ResInfo("IN_", ["CG", "NE1", "CZ2"]),
    "TYR": ResInfo("P__", ["CG", "CE1", "CE2"]),
    "PHE": ResInfo("P__", ["CG", "CE1", "CE2"])
}

def rays_from_residue(res):
    """Get ray pair characterizing the cation-pi interaction site of
    a residue.

    Parameters
    ----------
    res : pyrosetta.rosetta.core.conformation.Residue
        Residue from which to extract rays.

    Returns
    -------
    tuple of np.ndarray
        Pair of rays characterizing the cation-pi interaction present
        in the given residue.
    """
    atoms = rsd_to_fxnl_grp[res.name3()].atoms
    xyzs = [np.array(res.xyz(atom)) for atom in atoms]

    ray1 = create_ray(xyzs[1], xyzs[0])
    ray2 = create_ray(xyzs[2], xyzs[0])

    return (ray1, ray2)

def rays(pose, selector):
    """Get cation-pi ray pairs for the residues indicated by the
    provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.Pose
        Target structure.
    selector : pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    -------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible cation-pi
        interactions in the selected subset of the pose.
    """
    selected = selector.apply(pose)

    rays = []

    for i in range(1, len(pose.residues) + 1):
        res = pose.residue(i)
        if (selected[i] and res.name3() in rsd_to_fxnl_grp):
            rays.append(rays_from_residue(res))

    return rays


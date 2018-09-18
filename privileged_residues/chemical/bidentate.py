import re

from .util import FunctionalGroup, ResInfo
from ..geometry import create_ray

from collections import defaultdict
from itertools import combinations, product

rsd_to_fxnl_grp = {
    "ASN": ResInfo("CA_", ["CG", "OD1", "ND2"]),
    "GLN": ResInfo("CA_", ["CD", "OE1", "NE2"]),
    "ASP": ResInfo("C__", ["CG", "OD1", "OD2"]),
    "GLU": ResInfo("C__", ["CD", "OE1", "OE2"]),
    # Use HD1/HE2 to determine which tautomer to use
    "HIS": ResInfo("I__", ["ND1", "CD2", "NE2"]),
    "ARG": ResInfo("G__", ["CZ", "NH1", "NH2"]),
    "SER": ResInfo("OH_", ["CB", "OG", "HG"]),
    "THR": ResInfo("OH_", ["CB", "OG1", "HG1"]),
    "TYR": ResInfo("OH_", ["CZ", "OH", "HH"]),
    "LYS": ResInfo("A__", ["NZ", "1HZ", "2HZ"])
}

def _n_rays(pose, selected):
    """Get backbone donor (H-N) rays for the selected residues.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selected : pyrosetta.rosetta.utility.vector1_bool
        List indicating the particular residues to process.

    Returns
    -------
    list of np.ndarray
        All of the backbone donor rays in the selected subset of the
        pose.
    """

    assert(len(pose.residues) == len(selected))

    rays = { }

    for i in range(1, len(pose.residues) + 1):
        if (selected[i]):
            rsd = pose.residue(i)

            N = rsd.atom_index("N")
            H = rsd.attached_H_begin(N)

            if (rsd.attached_H_end(N) > 0):
                rays[i] = create_ray(rsd.xyz(H), rsd.xyz(N))

    return rays

def _c_rays(pose, selected):
    """Get backbone acceptor (O-C) rays for the selected residues.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selected : pyrosetta.rosetta.utility.vector1_bool
        List indicating the particular residues to process.

    Returns
    -------
    list of np.ndarray
        All of the backbone acceptor rays in the selected subset of the
        pose.
    """

    assert(len(pose.residues) == len(selected))

    rays = { }

    for i in range(1, len(pose.residues) + 1):
        if (selected[i]):
            rsd = pose.residue(i)

            C = rsd.atom_index("C")
            O = rsd.atom_index("O")

            rays[i] = create_ray(rsd.xyz(O), rsd.xyz(C))

    return rays

def _sc_donor(pose, selected):
    """Get sidechain donor (N-H) rays for the selected residues.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selected : pyrosetta.rosetta.utility.vector1_bool
        List indicating the particular residues to process.

    Returns
    -------
    list of np.ndarray
        All of the sidechain donor rays in the selected subset of the
        pose.
    """

    assert(len(pose.residues) == len(selected))

    rays = defaultdict(list)

    reg = re.compile(r"[NO]")

    for i in range(1, len(pose.residues) + 1):
        if (selected[i]):
            rsd = pose.residue(i)

            for j in range(rsd.first_sidechain_atom(), rsd.natoms() + 1):
                is_eneg = reg.search(rsd.atom_name(j))

                if (is_eneg and rsd.heavyatom_has_polar_hydrogens(j)):
                    for hatm in range(rsd.attached_H_begin(j), rsd.attached_H_end(j) + 1):
                        rays[i].append(create_ray(rsd.xyz(hatm), rsd.xyz(j)))

    return rays

def _sc_acceptor(pose, selected):
    """Get sidechain acceptor (O-C) rays for the selected residues.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selected : pyrosetta.rosetta.utility.vector1_bool
        List indicating the particular residues to process.

    Returns
    -------
    list of np.ndarray
        All of the sidechain acceptor rays in the selected subset of the
        pose.
    """

    assert(len(pose.residues) == len(selected))

    rays = defaultdict(list)

    reg = re.compile(r"[NO]")

    for i in range(1, len(pose.residues) + 1):
        if (selected[i]):
            rsd = pose.residue(i)

            for j in range(rsd.first_sidechain_atom(), rsd.natoms() + 1):
                is_eneg = reg.search(rsd.atom_name(j))
                batm = rsd.atom_base(j)

                if (is_eneg and rsd.heavyatom_is_an_acceptor(j)):
                    rays[i].append(create_ray(rsd.xyz(j), rsd.xyz(batm)))

    return rays

def sc_bb_rays(pose, selector):
    """Get sidechain-to-backbone ray pairs for the residues indicated
    by the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector : pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    ------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible
        sidechain-to-backbone interactions in the selected subset of the
        pose.
    """

    selected = selector.apply(pose)

    nrays = _n_rays(pose, selected)
    crays = _c_rays(pose, selected)

    rays = []

    for i in nrays:
        if (i - 1 in crays):
            rays.append((nrays[i], crays[i - 1]))

        rays.append((nrays[i], crays[i]))

    return rays

def sc_scbb_rays(pose, selector):
    """Get sidechain-to-sidechain-and-backbone ray pairs for the
    residues indicated by the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector : pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    ------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible
        sidechain-to-sidechain-and-backbone interactions in the selected
        subset of the pose.
    """

    selected = selector.apply(pose)

    nrays = _n_rays(pose, selected)
    crays = _c_rays(pose, selected)

    sc_acc = _sc_acceptor(pose, selected)
    sc_don = _sc_donor(pose, selected)

    rays = []

    for i in nrays:
        for jray in sc_acc[i] + sc_don[i]:
            rays.append((nrays[i], jray))
            rays.append((jray, crays[i]))

    return rays

def sc_sc_rays(pose, selector):
    """Get sidechain-to-sidechain ray pairs for the residues indicated
    by the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector : pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    ------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible
        sidechain-to-sidechain interactions in the selected subset of
        the pose.
    """

    selected = selector.apply(pose)

    sc_acc = _sc_acceptor(pose, selected)
    sc_don = _sc_donor(pose, selected)

    rays = []

    for i in range(1, len(pose.residues) + 1):
        for (jray, kray) in product(sc_don[i], sc_acc[i]):
            rays.append((jray, kray))

        for (jray, kray) in combinations(sc_don[i], 2):
            rays.append((jray, kray))

        for (jray, kray) in combinations(sc_acc[i], 2):
            rays.append((jray, kray))

    return rays

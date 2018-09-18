from .bidentate import _sc_donor, _sc_acceptor

from itertools import product

def donor_donor_rays(pose, selector):
    """Get donor-donor network ray pairs for the residues indicated by
    the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector: pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    -------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible donor-donor
        network interactions in the selected subset of the pose.
    """

    selected = selector.apply(pose)

    sc_don = _sc_donor(pose, selected)

    rays = []

    for (i, j) in product(sc_don.keys(), sc_don.keys()):
        if (i != j):
            for (kray, lray) in product(sc_don[i], sc_don[j]):
                rays.append((kray, lray))

    return rays

def acceptor_acceptor_rays(pose, selector):
    """Get acceptor-acceptor network ray pairs for the residues
    indicated by the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector: pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    -------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible
        acceptor-acceptor network interactions in the selected subset
        of the pose.
    """

    selected = selector.apply(pose)

    sc_acc = _sc_acceptor(pose, selected)

    rays = []

    for (i, j) in product(sc_acc.keys(), sc_acc.keys()):
        if (i != j):
            for (kray, lray) in product(sc_acc[i], sc_acc[j]):
                rays.append((kray, lray))

    return rays

def donor_acceptor_rays(pose, selector):
    """Get donor-acceptor network ray pairs for the residues indicated
    by the provided residue selector.

    Parameters
    ----------
    pose : pyrosetta.pose
        Target structure.
    selector: pyrosetta.rosetta.core.select.residue_selector.ResidueSelector
        Residue selector to apply to the pose.

    Returns
    -------
    list of tuple of np.ndarray
        All of the ray pairs corresponding to possible donor-acceptor
        network interactions in the selected subset of the pose.
    """

    selected = selector.apply(pose)

    sc_acc = _sc_acceptor(pose, selected)
    sc_don = _sc_donor(pose, selected)

    rays = []

    for (i, j) in product(sc_don.keys(), sc_acc.keys()):
        if (i != j):
            for (kray, lray) in product(sc_don[i], sc_acc[j]):
                rays.append((kray, lray))

    return rays


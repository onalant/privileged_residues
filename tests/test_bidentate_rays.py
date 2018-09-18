import pytest

import pyrosetta

from .data.residues import (
    ALA, ARG, ASN, ASP, CYS,
    CYZ, GLN, GLU, GLY, HIS_D,
    HIS, ILE, LEU, LYS, MET,
    PHE, PRO, SER, THR, TRP,
    TYR, VAL
)
from numpy.testing import assert_allclose

from privileged_residues import chemical

selector = pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()

@pytest.fixture(scope="module", params=[
    ALA, ARG, ASN, ASP, CYS,
    CYZ, GLN, GLU, GLY, HIS_D,
    HIS, ILE, LEU, LYS, MET,
    PHE, PRO, SER, THR, TRP,
    TYR, VAL
], ids=lambda p: p.name)
def dummy(request):
    return request.param

def test_sc_bb(dummy):
    sc_bb = [
        (dummy.n_rays[1], dummy.c_rays[1])
    ]

    if (dummy.name != "PRO"):
        sc_bb.extend([
            (dummy.n_rays[2], dummy.c_rays[1]),
            (dummy.n_rays[2], dummy.c_rays[2])
        ])

    sc_bb.extend([
        (dummy.n_rays[3], dummy.c_rays[2]),
        (dummy.n_rays[3], dummy.c_rays[3])
    ])

    rays = chemical.sc_bb_rays(dummy.pose, selector)

    assert_allclose(rays, sc_bb)

def test_sc_scbb(dummy):
    sc_scbb = [ ]

    if (dummy.name != "PRO"):
        sc_acceptors = dummy.sc_acceptor[2] if len(dummy.sc_acceptor) else [ ]
        sc_donors = dummy.sc_donor[2] if len(dummy.sc_donor) else [ ]

        for sc_ray in sc_acceptors + sc_donors:
            sc_scbb.extend([
                (dummy.n_rays[2], sc_ray),
                (sc_ray, dummy.c_rays[2])
            ])

    rays = chemical.sc_scbb_rays(dummy.pose, selector)

    assert_allclose(rays, sc_scbb)

def test_sc_sc(dummy):
    sc_sc = [ ]

    sc_acceptors = dummy.sc_acceptor[2] if len(dummy.sc_acceptor) else [ ]
    sc_donors = dummy.sc_donor[2] if len(dummy.sc_donor) else [ ]

    for sc_don in sc_donors:
        sc_sc.extend([
            (sc_don, sc_acc) for sc_acc in sc_acceptors
        ])

    for i in range(len(sc_donors)):
        sc_sc.extend([
            (sc_donors[i], sc_donors[i + j]) for j in range(1, len(sc_donors) - i)
        ])

    for i in range(len(sc_acceptors)):
        sc_sc.extend([
            (sc_acceptors[i], sc_acceptors[i + j]) for j in range(1, len(sc_acceptors) - i)
        ])

    rays = chemical.sc_sc_rays(dummy.pose, selector)

    assert_allclose(rays, sc_sc)

import pytest

from numpy.testing import assert_allclose

from privileged_residues.chemical import bidentate

def test_sc_bb(dummy_res, selector):
    sc_bb = [
        (dummy_res.n_rays[1], dummy_res.c_rays[1])
    ]

    if (dummy_res.name != "PRO"):
        sc_bb.extend([
            (dummy_res.n_rays[2], dummy_res.c_rays[1]),
            (dummy_res.n_rays[2], dummy_res.c_rays[2])
        ])

    sc_bb.extend([
        (dummy_res.n_rays[3], dummy_res.c_rays[2]),
        (dummy_res.n_rays[3], dummy_res.c_rays[3])
    ])

    rays = bidentate.sc_bb_rays(dummy_res.pose, selector)

    assert_allclose(rays, sc_bb)

def test_sc_scbb(dummy_res, selector):
    sc_scbb = [ ]

    if (dummy_res.name != "PRO"):
        sc_acceptors = dummy_res.sc_acceptor[2] if len(dummy_res.sc_acceptor) else [ ]
        sc_donors = dummy_res.sc_donor[2] if len(dummy_res.sc_donor) else [ ]

        for sc_ray in sc_acceptors + sc_donors:
            sc_scbb.extend([
                (dummy_res.n_rays[2], sc_ray),
                (sc_ray, dummy_res.c_rays[2])
            ])

    rays = bidentate.sc_scbb_rays(dummy_res.pose, selector)

    assert_allclose(rays, sc_scbb)

def test_sc_sc(dummy_res, selector):
    sc_sc = [ ]

    sc_acceptors = dummy_res.sc_acceptor[2] if len(dummy_res.sc_acceptor) else [ ]
    sc_donors = dummy_res.sc_donor[2] if len(dummy_res.sc_donor) else [ ]

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

    rays = bidentate.sc_sc_rays(dummy_res.pose, selector)

    assert_allclose(rays, sc_sc)

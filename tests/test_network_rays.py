import pytest

from numpy.testing import assert_allclose

from privileged_residues.chemical import network

def test_acceptor_acceptor(dummy_net, selector):
    acc_acc = [ ]

    sc_accA = dummy_net.sc_acceptor[1] if (1 in dummy_net.sc_acceptor) else [ ]
    sc_accB = dummy_net.sc_acceptor[2] if (2 in dummy_net.sc_acceptor) else [ ]

    for elemA in sc_accA:
        acc_acc.extend([
            (elemA, elemB) for elemB in sc_accB
        ])

    for elemB in sc_accB:
        acc_acc.extend([
            (elemB, elemA) for elemA in sc_accA
        ])

    rays = network.acceptor_acceptor_rays(dummy_net.pose, selector)

    assert_allclose(rays, acc_acc)

def test_donor_acceptor(dummy_net, selector):
    don_acc = [ ]

    sc_donA = dummy_net.sc_donor[1] if (1 in dummy_net.sc_donor) else [ ]
    sc_accA = dummy_net.sc_acceptor[1] if (1 in dummy_net.sc_acceptor) else [ ]

    sc_donB = dummy_net.sc_donor[2] if (2 in dummy_net.sc_donor) else [ ]
    sc_accB = dummy_net.sc_acceptor[2] if (2 in dummy_net.sc_acceptor) else [ ]

    for elemA in sc_donA:
        don_acc.extend([
            (elemA, elemB) for elemB in sc_accB
        ])

    for elemB in sc_donB:
        don_acc.extend([
            (elemB, elemA) for elemA in sc_accA
        ])

    rays = network.donor_acceptor_rays(dummy_net.pose, selector)

    assert_allclose(rays, don_acc)

def test_donor_donor(dummy_net, selector):
    don_don = [ ]

    sc_donA = dummy_net.sc_donor[1] if (1 in dummy_net.sc_donor) else [ ]
    sc_donB = dummy_net.sc_donor[2] if (2 in dummy_net.sc_donor) else [ ]

    for elemA in sc_donA:
        don_don.extend([
            (elemA, elemB) for elemB in sc_donB
        ])

    for elemB in sc_donB:
        don_don.extend([
            (elemB, elemA) for elemA in sc_donA
        ])

    rays = network.donor_donor_rays(dummy_net.pose, selector)

    assert_allclose(rays, don_don)

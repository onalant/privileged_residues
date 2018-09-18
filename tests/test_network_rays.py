import pytest

import pyrosetta

from .data.networks import (
    A_CA, A_C, A_OH, CA_A, CA_CA,
    CA_C, CA_G, CA_OH, C_A, C_CA,
    C_G, C_OH, G_CA, G_C, G_OH,
    OH_A, OH_CA, OH_C, OH_G, OH_OH
)
from numpy.testing import assert_allclose

from privileged_residues import chemical

selector = pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()

@pytest.fixture(scope="module", params=[
    A_CA, A_C, A_OH, CA_A, CA_CA,
    CA_C, CA_G, CA_OH, C_A, C_CA,
    C_G, C_OH, G_CA, G_C, G_OH,
    OH_A, OH_CA, OH_C, OH_G, OH_OH
], ids=lambda p: p.name)
def dummy(request):
    return request.param

def test_acceptor_acceptor(dummy):
    acc_acc = [ ]

    sc_accA = dummy.sc_acceptor[1] if (1 in dummy.sc_acceptor) else [ ]
    sc_accB = dummy.sc_acceptor[2] if (2 in dummy.sc_acceptor) else [ ]

    for elemA in sc_accA:
        acc_acc.extend([
            (elemA, elemB) for elemB in sc_accB
        ])

    for elemB in sc_accB:
        acc_acc.extend([
            (elemB, elemA) for elemA in sc_accA
        ])

    rays = chemical.acceptor_acceptor_rays(dummy.pose, selector)

    assert_allclose(rays, acc_acc)

def test_donor_acceptor(dummy):
    don_acc = [ ]

    sc_donA = dummy.sc_donor[1] if (1 in dummy.sc_donor) else [ ]
    sc_accA = dummy.sc_acceptor[1] if (1 in dummy.sc_acceptor) else [ ]

    sc_donB = dummy.sc_donor[2] if (2 in dummy.sc_donor) else [ ]
    sc_accB = dummy.sc_acceptor[2] if (2 in dummy.sc_acceptor) else [ ]

    for elemA in sc_donA:
        don_acc.extend([
            (elemA, elemB) for elemB in sc_accB
        ])

    for elemB in sc_donB:
        don_acc.extend([
            (elemB, elemA) for elemA in sc_accA
        ])

    rays = chemical.donor_acceptor_rays(dummy.pose, selector)

    assert_allclose(rays, don_acc)

def test_donor_donor(dummy):
    don_don = [ ]

    sc_donA = dummy.sc_donor[1] if (1 in dummy.sc_donor) else [ ]
    sc_donB = dummy.sc_donor[2] if (2 in dummy.sc_donor) else [ ]

    for elemA in sc_donA:
        don_don.extend([
            (elemA, elemB) for elemB in sc_donB
        ])

    for elemB in sc_donB:
        don_don.extend([
            (elemB, elemA) for elemA in sc_donA
        ])

    rays = chemical.donor_donor_rays(dummy.pose, selector)

    assert_allclose(rays, don_don)

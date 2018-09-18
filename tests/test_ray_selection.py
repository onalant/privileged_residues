import pytest

import pyrosetta

from .data.residues import (
    ALA, ARG, ASN, ASP, CYS,
    CYZ, GLN, GLU, GLY, HIS_D,
    HIS, ILE, LEU, LYS, MET,
    PHE, PRO, SER, THR, TRP,
    TYR, VAL
)
from .util import rays_allclose

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

def test_n_rays(dummy):
    selected = selector.apply(dummy.pose)

    rays = chemical._n_rays(dummy.pose, selected)

    rays_allclose(rays, dummy.n_rays)

def test_c_rays(dummy):
    selected = selector.apply(dummy.pose)

    rays = chemical._c_rays(dummy.pose, selected)

    rays_allclose(rays, dummy.c_rays)

def test_sc_donor(dummy):
    selected = selector.apply(dummy.pose)

    rays = chemical._sc_donor(dummy.pose, selected)

    rays_allclose(rays, dummy.sc_donor)

def test_sc_acceptor(dummy):
    selected = selector.apply(dummy.pose)

    rays = chemical._sc_acceptor(dummy.pose, selected)

    rays_allclose(rays, dummy.sc_acceptor)


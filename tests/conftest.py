import pytest

import pyrosetta

@pytest.fixture
def selector():
    return pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()

from .data.residues import (
    ALA, ARG, ASN, ASP, CYS,
    CYZ, GLN, GLU, GLY, HIS_D,
    HIS, ILE, LEU, LYS, MET,
    PHE, PRO, SER, THR, TRP,
    TYR, VAL
)

@pytest.fixture(scope="module", params=[
    ALA, ARG, ASN, ASP, CYS,
    CYZ, GLN, GLU, GLY, HIS_D,
    HIS, ILE, LEU, LYS, MET,
    PHE, PRO, SER, THR, TRP,
    TYR, VAL
], ids=lambda p: p.name)
def dummy_res(request):
    return request.param

from .data.networks import (
    A_CA, A_C, A_OH, CA_A, CA_CA,
    CA_C, CA_G, CA_OH, C_A, C_CA,
    C_G, C_OH, G_CA, G_C, G_OH,
    OH_A, OH_CA, OH_C, OH_G, OH_OH
)

@pytest.fixture(scope="module", params=[
    A_CA, A_C, A_OH, CA_A, CA_CA,
    CA_C, CA_G, CA_OH, C_A, C_CA,
    C_G, C_OH, G_CA, G_C, G_OH,
    OH_A, OH_CA, OH_C, OH_G, OH_OH
], ids=lambda p: p.name)
def dummy_net(request):
    return request.param

import dask

from multiprocessing.pool import ThreadPool

dask.config.set(pool=ThreadPool(4))

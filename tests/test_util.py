import pytest

import numpy as np

from privileged_residues import util

from tests.util import pick_ray

from numpy.testing import assert_allclose

from os import path

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring
from pyrosetta.rosetta.numeric import xyzVector_double_t as V3

from rif.geom import Ray

contents = """
ATOM      1  N   ALA A   1       0.000   0.000   0.000  1.00  0.00           N
ATOM      2  CA  ALA A   1       1.458   0.000   0.000  1.00  0.00           C
ATOM      3  C   ALA A   1       2.009   1.420   0.000  1.00  0.00           C
ATOM      4  O   ALA A   1       1.251   2.390   0.000  1.00  0.00           O
ATOM      5  CB  ALA A   1       1.988  -0.773  -1.199  1.00  0.00           C
ATOM      6 1H   ALA A   1      -0.334  -0.943  -0.000  1.00  0.00           H
ATOM      7 2H   ALA A   1      -0.334   0.471   0.816  1.00  0.00           H
ATOM      8 3H   ALA A   1      -0.334   0.471  -0.816  1.00  0.00           H
ATOM      9  HA  ALA A   1       1.797  -0.490   0.913  1.00  0.00           H
ATOM     10 1HB  ALA A   1       3.078  -0.764  -1.185  1.00  0.00           H
ATOM     11 2HB  ALA A   1       1.633  -1.802  -1.154  1.00  0.00           H
ATOM     12 3HB  ALA A   1       1.633  -0.307  -2.117  1.00  0.00           H
"""

@pytest.fixture
def dummy():
    p = Pose()
    pose_from_pdbstring(p, contents)

    return p

def test_pick_ray(dummy):
    backbone_n = np.array([
        [-0.334, -0.334],
        [-0.943, -0.943],
        [0.000, 0.000],
        [1.000, 0.000]
    ])

    backbone_c = np.array([
        [1.251, -0.616],
        [2.390, 0.788],
        [0.000, 0.000],
        [1.000, 0.000]
    ])

    assert_allclose(backbone_n, pick_ray(dummy.residue(1), "1H", "N"), atol=1e-3)
    assert_allclose(backbone_c, pick_ray(dummy.residue(1), "O", "C"), atol=1e-3)

def test_apply_transform(dummy):
    xform = np.identity(4)
    xform[:3, 3] = 1

    a = np.eye(1, 3, 0)
    b = np.eye(1, 3, 1)
    K = np.outer(b, a) - np.outer(a, b)
    angle = 2 * np.pi * np.random.random()

    xform[:3, :3] = np.identity(3) + np.sin(angle) * K + (1 - np.cos(angle)) * (K @ K)

    ori_coords = np.ones((4, dummy.total_atoms()))
    ori_coords[:3] = np.array([atom.xyz() for residue in dummy.residues for atom in residue.atoms()]).T

    dummy.apply_transform(xform)

    mod_coords = np.ones((4, dummy.total_atoms()))
    mod_coords[:3] = np.array([atom.xyz() for residue in dummy.residues for atom in residue.atoms()]).T

    assert_allclose(mod_coords, xform @ ori_coords)

def test_xyzVector_iter():
    for i in range(100):
        data = np.random.random(3)
        vec = V3(*data)

        assert_allclose([*vec], [*data])

def test_numpy_to_rif():
    for i in range(100):
        numpy_ray = np.random.random((4, 2)).astype("f4")

        rif_ray = util.numpy_to_rif(numpy_ray)

        assert_allclose(rif_ray[0][0][0], numpy_ray)

def test_models_pdb(dummy):
    for mdl in util.models_from_pdb(path.join(path.dirname(__file__), "data/dummy_models.pdb")):
        for i in range(1, len(mdl.residues) + 1):
            for j in range(1, mdl.residue(i).natoms() + 1):
                assert([*mdl.residue(i).xyz(j)] == [*dummy.residue(i).xyz(j)])
                assert(mdl.residue(i).atom_name(j) == dummy.residue(i).atom_name(j))

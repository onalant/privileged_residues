import pytest

import numpy as np
import pyrosetta

from privileged_residues import PrivilegedResidues
from privileged_residues.chemical.bidentate import rsd_to_fxnl_grp
from privileged_residues.chemical.util import functional_groups

from os import path

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring
from rmsd import rmsd

contents = """
ATOM      1  N   GLY A   1      -0.922  -0.288   2.818  1.00  0.00           N
ATOM      2  CA  GLY A   1       0.276  -1.086   2.588  1.00  0.00           C
ATOM      3  C   GLY A   1       1.262  -0.351   1.688  1.00  0.00           C
ATOM      4  O   GLY A   1       2.421  -0.153   2.053  1.00  0.00           O
ATOM      5 1H   GLY A   1      -1.551  -0.792   3.410  1.00  0.00           H
ATOM      6 2H   GLY A   1      -0.670   0.574   3.258  1.00  0.00           H
ATOM      7 3H   GLY A   1      -1.369  -0.097   1.944  1.00  0.00           H
ATOM      8 1HA  GLY A   1       0.750  -1.315   3.543  1.00  0.00           H
ATOM      9 2HA  GLY A   1      -0.001  -2.035   2.131  1.00  0.00           H
ATOM     10  N   ASN A   2       0.795   0.050   0.511  1.00  0.00           N
ATOM     11  CA  ASN A   2       1.687   0.450  -0.571  1.00  0.00           C
ATOM     12  C   ASN A   2       1.060   1.544  -1.426  1.00  0.00           C
ATOM     13  O   ASN A   2       1.215   1.558  -2.647  1.00  0.00           O
ATOM     14  CB  ASN A   2       2.060  -0.747  -1.426  1.00  0.00           C
ATOM     15  CG  ASN A   2       0.866  -1.379  -2.086  1.00  0.00           C
ATOM     16  OD1 ASN A   2      -0.268  -1.230  -1.618  1.00  0.00           O
ATOM     17  ND2 ASN A   2       1.100  -2.085  -3.163  1.00  0.00           N
ATOM     18  H   ASN A   2      -0.203   0.079   0.361  1.00  0.00           H
ATOM     19  HA  ASN A   2       2.598   0.863  -0.135  1.00  0.00           H
ATOM     20 1HB  ASN A   2       2.765  -0.438  -2.198  1.00  0.00           H
ATOM     21 2HB  ASN A   2       2.557  -1.495  -0.808  1.00  0.00           H
ATOM     22 1HD2 ASN A   2       0.343  -2.529  -3.645  1.00  0.00           H
ATOM     23 2HD2 ASN A   2       2.035  -2.179  -3.506  1.00  0.00           H
ATOM     24  N   GLY A   3       0.352   2.462  -0.776  1.00  0.00           N
ATOM     25  CA  GLY A   3      -0.304   3.560  -1.476  1.00  0.00           C
ATOM     26  C   GLY A   3       0.448   4.869  -1.277  1.00  0.00           C
ATOM     27  O   GLY A   3       0.071   5.694  -0.443  1.00  0.00           O
ATOM     28  OXT GLY A   3       1.421   5.109  -1.937  1.00  0.00           O
ATOM     29  H   GLY A   3       0.267   2.398   0.228  1.00  0.00           H
ATOM     30 1HA  GLY A   3      -0.365   3.330  -2.540  1.00  0.00           H
ATOM     31 2HA  GLY A   3      -1.327   3.665  -1.112  1.00  0.00           H
TER
ATOM     33  N   GLY B   4      -4.694  -3.383  -0.196  1.00  0.00           N
ATOM     34  CA  GLY B   4      -3.419  -3.112  -0.850  1.00  0.00           C
ATOM     35  C   GLY B   4      -3.620  -2.702  -2.304  1.00  0.00           C
ATOM     36  O   GLY B   4      -4.652  -3.000  -2.905  1.00  0.00           O
ATOM     37 1H   GLY B   4      -4.532  -3.649   0.754  1.00  0.00           H
ATOM     38 2H   GLY B   4      -5.263  -2.561  -0.220  1.00  0.00           H
ATOM     39 3H   GLY B   4      -5.163  -4.125  -0.675  1.00  0.00           H
ATOM     40 1HA  GLY B   4      -2.896  -2.319  -0.314  1.00  0.00           H
ATOM     41 2HA  GLY B   4      -2.789  -4.000  -0.802  1.00  0.00           H
ATOM     42  N   GLY B   5      -2.628  -2.019  -2.862  1.00  0.00           N
ATOM     43  CA  GLY B   5      -2.695  -1.567  -4.247  1.00  0.00           C
ATOM     44  C   GLY B   5      -2.125  -2.613  -5.197  1.00  0.00           C
ATOM     45  O   GLY B   5      -1.147  -3.288  -4.878  1.00  0.00           O
ATOM     46  H   GLY B   5      -1.807  -1.806  -2.315  1.00  0.00           H
ATOM     47 1HA  GLY B   5      -3.731  -1.356  -4.512  1.00  0.00           H
ATOM     48 2HA  GLY B   5      -2.141  -0.635  -4.353  1.00  0.00           H
ATOM     49  N   GLY B   6      -2.743  -2.741  -6.366  1.00  0.00           N
ATOM     50  CA  GLY B   6      -2.247  -3.641  -7.399  1.00  0.00           C
ATOM     51  C   GLY B   6      -2.270  -2.973  -8.769  1.00  0.00           C
ATOM     52  O   GLY B   6      -2.348  -3.646  -9.797  1.00  0.00           O
ATOM     53  OXT GLY B   6      -2.213  -1.778  -8.855  1.00  0.00           O
ATOM     54  H   GLY B   6      -3.579  -2.201  -6.543  1.00  0.00           H
ATOM     55 1HA  GLY B   6      -1.229  -3.949  -7.158  1.00  0.00           H
ATOM     56 2HA  GLY B   6      -2.858  -4.543  -7.420  1.00  0.00           H
TER
"""

@pytest.fixture
def dummy():
    p = Pose()
    pose_from_pdbstring(p, contents)

    return p

@pytest.fixture
def selector():
    return pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()

def test_match(dummy, selector):
    pr = PrivilegedResidues(path.join(path.dirname(__file__), "data/DUMMY.zarr/"))

    res = dummy.residue(2)
    expected_coords = np.array([res.xyz(atom) for atom in rsd_to_fxnl_grp[res.name3()].atoms])

    for (_, match) in pr.search(dummy, selector, groups=["sc_bb"]):
        rmatch = match.residue(1)
        coords = np.array([rmatch.xyz(atom) for atom in functional_groups[rmatch.name()].atoms])

        if (rmsd(coords, expected_coords) < 0.1):
            return

    assert()

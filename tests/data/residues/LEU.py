from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "LEU"

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
ATOM     13  N   LEU A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  LEU A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   LEU A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   LEU A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  LEU A   2       3.546   3.654   1.222  1.00  0.00           C
ATOM     18  CG  LEU A   2       2.546   2.962   2.157  1.00  0.00           C
ATOM     19  CD1 LEU A   2       2.223   1.575   1.620  1.00  0.00           C
ATOM     20  CD2 LEU A   2       3.134   2.882   3.559  1.00  0.00           C
ATOM     21  H   LEU A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     22  HA  LEU A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     23 1HB  LEU A   2       4.428   3.906   1.808  1.00  0.00           H
ATOM     24 2HB  LEU A   2       3.089   4.580   0.875  1.00  0.00           H
ATOM     25  HG  LEU A   2       1.618   3.533   2.185  1.00  0.00           H
ATOM     26 1HD1 LEU A   2       1.513   1.083   2.284  1.00  0.00           H
ATOM     27 2HD1 LEU A   2       1.787   1.662   0.625  1.00  0.00           H
ATOM     28 3HD1 LEU A   2       3.137   0.984   1.565  1.00  0.00           H
ATOM     29 1HD2 LEU A   2       2.423   2.391   4.224  1.00  0.00           H
ATOM     30 2HD2 LEU A   2       4.061   2.310   3.533  1.00  0.00           H
ATOM     31 3HD2 LEU A   2       3.338   3.888   3.925  1.00  0.00           H
ATOM     32  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     33  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     34  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     35  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     36  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     37  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     38  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     39  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     40 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     41 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     42 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
TER
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

n_rays = {
    1: pick_ray(pose.residue(1), "1H", "N"),
    2: pick_ray(pose.residue(2), "H", "N"),
    3: pick_ray(pose.residue(3), "H", "N")
}

c_rays = {
    1: pick_ray(pose.residue(1), "O", "C"),
    2: pick_ray(pose.residue(2), "O", "C"),
    3: pick_ray(pose.residue(3), "O", "C")
}

sc_donor = { }

sc_acceptor = { }

cat_pi = [ ]

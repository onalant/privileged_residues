from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "ALA"

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
ATOM     13  N   ALA A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  ALA A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   ALA A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   ALA A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  ALA A   2       3.535   3.659   1.199  1.00  0.00           C
ATOM     18  H   ALA A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     19  HA  ALA A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     20 1HB  ALA A   2       4.033   4.629   1.185  1.00  0.00           H
ATOM     21 2HB  ALA A   2       2.456   3.805   1.154  1.00  0.00           H
ATOM     22 3HB  ALA A   2       3.792   3.133   2.117  1.00  0.00           H
ATOM     23  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     24  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     25  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     26  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     27  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     28  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     29  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     30  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     31 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     32 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     33 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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

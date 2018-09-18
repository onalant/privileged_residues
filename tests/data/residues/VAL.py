from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "VAL"

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
ATOM     13  N   VAL A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  VAL A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   VAL A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   VAL A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  VAL A   2       3.553   3.655   1.232  1.00  0.00           C
ATOM     18  CG1 VAL A   2       2.572   2.859   2.079  1.00  0.00           C
ATOM     19  CG2 VAL A   2       4.775   4.050   2.048  1.00  0.00           C
ATOM     20  H   VAL A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     21  HA  VAL A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     22  HB  VAL A   2       3.034   4.553   0.896  1.00  0.00           H
ATOM     23 1HG1 VAL A   2       2.275   3.452   2.945  1.00  0.00           H
ATOM     24 2HG1 VAL A   2       1.690   2.619   1.485  1.00  0.00           H
ATOM     25 3HG1 VAL A   2       3.046   1.938   2.416  1.00  0.00           H
ATOM     26 1HG2 VAL A   2       4.460   4.627   2.917  1.00  0.00           H
ATOM     27 2HG2 VAL A   2       5.297   3.152   2.379  1.00  0.00           H
ATOM     28 3HG2 VAL A   2       5.443   4.653   1.434  1.00  0.00           H
ATOM     29  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     30  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     31  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     32  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     33  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     34  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     35  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     36  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     37 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     38 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     39 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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

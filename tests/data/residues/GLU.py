from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "GLU"

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
ATOM     13  N   GLU A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  GLU A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   GLU A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   GLU A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  GLU A   2       3.544   3.658   1.214  1.00  0.00           C
ATOM     18  CG  GLU A   2       2.549   2.950   2.121  1.00  0.00           C
ATOM     19  CD  GLU A   2       2.195   1.571   1.638  1.00  0.00           C
ATOM     20  OE1 GLU A   2       2.709   1.168   0.622  1.00  0.00           O
ATOM     21  OE2 GLU A   2       1.411   0.919   2.287  1.00  0.00           O
ATOM     22  H   GLU A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     23  HA  GLU A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     24 1HB  GLU A   2       4.416   3.921   1.814  1.00  0.00           H
ATOM     25 2HB  GLU A   2       3.087   4.589   0.877  1.00  0.00           H
ATOM     26 1HG  GLU A   2       2.974   2.875   3.121  1.00  0.00           H
ATOM     27 2HG  GLU A   2       1.642   3.551   2.187  1.00  0.00           H
ATOM     28  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     29  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     30  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     31  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     32  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     33  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     34  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     35  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     36 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     37 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     38 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OE1", "CD"),
        pick_ray(pose.residue(2), "OE2", "CD")
    ]
}

cat_pi = [ ]

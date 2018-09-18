from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "ILE"

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
ATOM     13  N   ILE A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  ILE A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   ILE A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   ILE A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  ILE A   2       3.552   3.673   1.218  1.00  0.00           C
ATOM     18  CG1 ILE A   2       2.555   2.887   2.075  1.00  0.00           C
ATOM     19  CG2 ILE A   2       2.946   4.994   0.770  1.00  0.00           C
ATOM     20  CD1 ILE A   2       2.241   1.510   1.536  1.00  0.00           C
ATOM     21  H   ILE A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     22  HA  ILE A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     23  HB  ILE A   2       4.417   3.876   1.849  1.00  0.00           H
ATOM     24 1HG1 ILE A   2       2.950   2.776   3.084  1.00  0.00           H
ATOM     25 2HG1 ILE A   2       1.621   3.444   2.149  1.00  0.00           H
ATOM     26 1HG2 ILE A   2       2.643   5.570   1.643  1.00  0.00           H
ATOM     27 2HG2 ILE A   2       3.685   5.558   0.201  1.00  0.00           H
ATOM     28 3HG2 ILE A   2       2.076   4.801   0.142  1.00  0.00           H
ATOM     29 1HD1 ILE A   2       1.528   1.015   2.196  1.00  0.00           H
ATOM     30 2HD1 ILE A   2       1.810   1.598   0.538  1.00  0.00           H
ATOM     31 3HD1 ILE A   2       3.156   0.921   1.486  1.00  0.00           H
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

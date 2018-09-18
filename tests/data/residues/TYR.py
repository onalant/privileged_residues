from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "TYR"

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
ATOM     13  N   TYR A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  TYR A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   TYR A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   TYR A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  TYR A   2       3.534   3.666   1.205  1.00  0.00           C
ATOM     18  CG  TYR A   2       2.537   2.955   2.093  1.00  0.00           C
ATOM     19  CD1 TYR A   2       2.119   1.671   1.777  1.00  0.00           C
ATOM     20  CD2 TYR A   2       2.040   3.588   3.222  1.00  0.00           C
ATOM     21  CE1 TYR A   2       1.207   1.022   2.587  1.00  0.00           C
ATOM     22  CE2 TYR A   2       1.129   2.939   4.033  1.00  0.00           C
ATOM     23  CZ  TYR A   2       0.713   1.661   3.719  1.00  0.00           C
ATOM     24  OH  TYR A   2      -0.195   1.015   4.526  1.00  0.00           O
ATOM     25  H   TYR A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     26  HA  TYR A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     27 1HB  TYR A   2       4.401   3.931   1.812  1.00  0.00           H
ATOM     28 2HB  TYR A   2       3.081   4.594   0.859  1.00  0.00           H
ATOM     29  HD1 TYR A   2       2.509   1.173   0.889  1.00  0.00           H
ATOM     30  HD2 TYR A   2       2.367   4.597   3.470  1.00  0.00           H
ATOM     31  HE1 TYR A   2       0.879   0.013   2.339  1.00  0.00           H
ATOM     32  HE2 TYR A   2       0.738   3.437   4.921  1.00  0.00           H
ATOM     33  HH  TYR A   2      -0.435   1.588   5.258  1.00  0.00           H
ATOM     34  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     35  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     36  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     37  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     38  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     39  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     40  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     41  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     42 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     43 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     44 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "HH", "OH")
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OH", "CZ")
    ]
}

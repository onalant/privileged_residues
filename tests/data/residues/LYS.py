from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "LYS"

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
ATOM     13  N   LYS A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  LYS A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   LYS A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   LYS A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  LYS A   2       3.539   3.664   1.207  1.00  0.00           C
ATOM     18  CG  LYS A   2       2.537   2.960   2.113  1.00  0.00           C
ATOM     19  CD  LYS A   2       2.207   1.568   1.595  1.00  0.00           C
ATOM     20  CE  LYS A   2       2.967   1.258   0.315  1.00  0.00           C
ATOM     21  NZ  LYS A   2       3.837   2.390  -0.105  1.00  0.00           N
ATOM     22  H   LYS A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     23  HA  LYS A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     24 1HB  LYS A   2       4.407   3.928   1.811  1.00  0.00           H
ATOM     25 2HB  LYS A   2       3.084   4.593   0.863  1.00  0.00           H
ATOM     26 1HG  LYS A   2       2.951   2.877   3.118  1.00  0.00           H
ATOM     27 2HG  LYS A   2       1.619   3.546   2.164  1.00  0.00           H
ATOM     28 1HD  LYS A   2       2.468   0.827   2.352  1.00  0.00           H
ATOM     29 2HD  LYS A   2       1.137   1.498   1.397  1.00  0.00           H
ATOM     30 1HE  LYS A   2       3.588   0.376   0.465  1.00  0.00           H
ATOM     31 2HE  LYS A   2       2.260   1.045  -0.486  1.00  0.00           H
ATOM     32 1HZ  LYS A   2       4.323   2.146  -0.956  1.00  0.00           H
ATOM     33 2HZ  LYS A   2       3.269   3.210  -0.265  1.00  0.00           H
ATOM     34 3HZ  LYS A   2       4.510   2.585   0.622  1.00  0.00           H
ATOM     35  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     36  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     37  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     38  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     39  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     40  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     41  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     42  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     43 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     44 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     45 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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
        pick_ray(pose.residue(2), "1HZ", "NZ"),
        pick_ray(pose.residue(2), "2HZ", "NZ"),
        pick_ray(pose.residue(2), "3HZ", "NZ")
    ]
}

sc_acceptor = { }

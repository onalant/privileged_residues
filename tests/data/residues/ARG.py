from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "ARG"

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
ATOM     13  N   ARG A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  ARG A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   ARG A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   ARG A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  ARG A   2       3.560   3.653   1.212  1.00  0.00           C
ATOM     18  CG  ARG A   2       2.572   2.957   2.134  1.00  0.00           C
ATOM     19  CD  ARG A   2       2.227   1.597   1.644  1.00  0.00           C
ATOM     20  NE  ARG A   2       2.920   1.275   0.407  1.00  0.00           N
ATOM     21  CZ  ARG A   2       3.774   2.100  -0.229  1.00  0.00           C
ATOM     22  NH1 ARG A   2       4.030   3.291   0.267  1.00  0.00           N
ATOM     23  NH2 ARG A   2       4.356   1.713  -1.351  1.00  0.00           N
ATOM     24  H   ARG A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     25  HA  ARG A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     26 1HB  ARG A   2       4.436   3.913   1.804  1.00  0.00           H
ATOM     27 2HB  ARG A   2       3.101   4.585   0.880  1.00  0.00           H
ATOM     28 1HG  ARG A   2       3.007   2.862   3.129  1.00  0.00           H
ATOM     29 2HG  ARG A   2       1.654   3.543   2.194  1.00  0.00           H
ATOM     30 1HD  ARG A   2       2.507   0.858   2.394  1.00  0.00           H
ATOM     31 2HD  ARG A   2       1.155   1.538   1.459  1.00  0.00           H
ATOM     32  HE  ARG A   2       2.749   0.368  -0.005  1.00  0.00           H
ATOM     33 1HH1 ARG A   2       3.586   3.587   1.125  1.00  0.00           H
ATOM     34 2HH1 ARG A   2       4.671   3.909  -0.209  1.00  0.00           H
ATOM     35 1HH2 ARG A   2       4.159   0.798  -1.732  1.00  0.00           H
ATOM     36 2HH2 ARG A   2       4.996   2.331  -1.827  1.00  0.00           H
ATOM     37  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     38  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     39  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     40  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     41  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     42  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     43  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     44  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     45 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     46 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     47 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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
        pick_ray(pose.residue(2), "HE", "NE"),
        pick_ray(pose.residue(2), "1HH1", "NH1"),
        pick_ray(pose.residue(2), "2HH1", "NH1"),
        pick_ray(pose.residue(2), "1HH2", "NH2"),
        pick_ray(pose.residue(2), "2HH2", "NH2")
    ]
}

sc_acceptor = { }

cat_pi = [
    (pick_ray(pose.residue(2), "NH1", "CZ"), pick_ray(pose.residue(2), "NH2", "CZ"))
]

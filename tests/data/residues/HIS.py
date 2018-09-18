from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "HIS"

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
ATOM     13  N   HIS A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  HIS A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   HIS A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   HIS A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  HIS A   2       3.548   3.665   1.213  1.00  0.00           C
ATOM     18  CG  HIS A   2       2.569   2.960   2.099  1.00  0.00           C
ATOM     19  ND1 HIS A   2       2.113   1.685   1.837  1.00  0.00           N
ATOM     20  CD2 HIS A   2       1.959   3.351   3.242  1.00  0.00           C
ATOM     21  CE1 HIS A   2       1.264   1.322   2.782  1.00  0.00           C
ATOM     22  NE2 HIS A   2       1.153   2.315   3.646  1.00  0.00           N
ATOM     23  H   HIS A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     24  HA  HIS A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     25 1HB  HIS A   2       4.422   3.927   1.810  1.00  0.00           H
ATOM     26 2HB  HIS A   2       3.093   4.595   0.874  1.00  0.00           H
ATOM     27  HD2 HIS A   2       2.083   4.309   3.748  1.00  0.00           H
ATOM     28  HE1 HIS A   2       0.744   0.366   2.840  1.00  0.00           H
ATOM     29  HE2 HIS A   2       0.571   2.317   4.472  1.00  0.00           H
ATOM     30  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     31  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     32  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     33  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     34  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     35  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     36  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     37  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     38 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     39 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     40 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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
        pick_ray(pose.residue(2), "HE2", "NE2")
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "ND1", "CG")
    ]
}

cat_pi = [
    (pick_ray(pose.residue(2), "CD2", "ND1"), pick_ray(pose.residue(2), "NE2", "ND1"))
]

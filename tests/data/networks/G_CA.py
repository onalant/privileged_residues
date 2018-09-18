from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "G_CA"

contents = """
HETNAM     G__ A   1  G__
HETNAM     CA_ A   2  CA_
HETATM    1  CV  G__ A   1       6.641   3.435  -1.700  1.00  0.00           X
HETATM    2  NE  G__ A   1       6.096   2.774  -2.875  1.00  0.00           N
HETATM    3  CZ  G__ A   1       5.981   1.438  -3.018  1.00  0.00           C
HETATM    4  NH1 G__ A   1       6.376   0.637  -2.053  1.00  0.00           N
HETATM    5  NH2 G__ A   1       5.475   0.937  -4.124  1.00  0.00           N
HETATM    6  HE  G__ A   1       5.781   3.357  -3.639  1.00  0.00           H
HETATM    7 1HH1 G__ A   1       6.765   1.026  -1.204  1.00  0.00           H
HETATM    8 2HH1 G__ A   1       6.290  -0.364  -2.162  1.00  0.00           H
HETATM    9 1HH2 G__ A   1       5.172   1.550  -4.865  1.00  0.00           H
HETATM   10 2HH2 G__ A   1       5.390  -0.064  -4.231  1.00  0.00           H
HETATM   11  CV  CA_ A   2       2.545  -0.632  -8.057  1.00  0.00           X
HETATM   12  CG  CA_ A   2       2.925  -0.394  -6.622  1.00  0.00           C
HETATM   13  OD1 CA_ A   2       3.599   0.596  -6.299  1.00  0.00           O
HETATM   14  ND2 CA_ A   2       2.505  -1.288  -5.738  1.00  0.00           N
HETATM   15 1HD2 CA_ A   2       2.729  -1.179  -4.767  1.00  0.00           H
HETATM   16 2HD2 CA_ A   2       1.964  -2.072  -6.039  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    6
CONECT    3    2    4    5
CONECT    4    3    7    8
CONECT    5    3    9   10
CONECT    6    2
CONECT    7    4
CONECT    8    4
CONECT    9    5
CONECT   10    5
CONECT   11   12
CONECT   12   11   13   14
CONECT   13   12
CONECT   14   12   15   16
CONECT   15   14
CONECT   16   14
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HE", "NE"),
        pick_ray(pose.residue(1), "1HH1", "NH1"),
        pick_ray(pose.residue(1), "2HH1", "NH1"),
        pick_ray(pose.residue(1), "1HH2", "NH2"),
        pick_ray(pose.residue(1), "2HH2", "NH2")
    ],
    2: [
        pick_ray(pose.residue(2), "1HD2", "ND2"),
        pick_ray(pose.residue(2), "2HD2", "ND2")
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OD1", "CG")
    ]
}

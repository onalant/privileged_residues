from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "G_C"

contents = """
HETNAM     G__ A   1  G__
HETNAM     C__ A   2  C__
HETATM    1  CV  G__ A   1      11.103  -5.324   0.225  1.00  0.00           X
HETATM    2  NE  G__ A   1      11.107  -3.872   0.139  1.00  0.00           N
HETATM    3  CZ  G__ A   1      10.031  -3.121  -0.165  1.00  0.00           C
HETATM    4  NH1 G__ A   1       8.875  -3.697  -0.409  1.00  0.00           N
HETATM    5  NH2 G__ A   1      10.137  -1.811  -0.218  1.00  0.00           N
HETATM    6  HE  G__ A   1      11.979  -3.393   0.320  1.00  0.00           H
HETATM    7 1HH1 G__ A   1       8.797  -4.706  -0.367  1.00  0.00           H
HETATM    8 2HH1 G__ A   1       8.068  -3.133  -0.637  1.00  0.00           H
HETATM    9 1HH2 G__ A   1      11.024  -1.368  -0.031  1.00  0.00           H
HETATM   10 2HH2 G__ A   1       9.330  -1.249  -0.446  1.00  0.00           H
HETATM   11  CV  C__ A   2       9.842  -4.360  -4.397  1.00  0.00           X
HETATM   12  CD  C__ A   2       8.947  -4.296  -3.191  1.00  0.00           C
HETATM   13  OE1 C__ A   2       8.358  -3.263  -2.964  1.00  0.00           O
HETATM   14  OE2 C__ A   2       8.851  -5.281  -2.494  1.00  0.00           O
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
CONECT   14   12
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
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OE1", "CD"),
        pick_ray(pose.residue(2), "OE2", "CD")
    ]
}

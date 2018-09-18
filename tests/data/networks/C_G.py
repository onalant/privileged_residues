from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "C_G"

contents = """
HETNAM     C__ A   1  C__
HETNAM     G__ A   2  G__
HETATM    1  CV  C__ A   1       9.822   1.552  -1.932  1.00  0.00           X
HETATM    2  CD  C__ A   1       8.392   1.160  -1.682  1.00  0.00           C
HETATM    3  OE1 C__ A   1       8.145   0.461  -0.726  1.00  0.00           O
HETATM    4  OE2 C__ A   1       7.545   1.561  -2.449  1.00  0.00           O
HETATM    5  CV  G__ A   2       5.665  -0.959  -7.271  1.00  0.00           X
HETATM    6  NE  G__ A   2       6.001   0.048  -6.277  1.00  0.00           N
HETATM    7  CZ  G__ A   2       5.337   0.231  -5.118  1.00  0.00           C
HETATM    8  NH1 G__ A   2       4.307  -0.532  -4.824  1.00  0.00           N
HETATM    9  NH2 G__ A   2       5.719   1.172  -4.283  1.00  0.00           N
HETATM   10  HE  G__ A   2       6.788   0.654  -6.469  1.00  0.00           H
HETATM   11 1HH1 G__ A   2       4.016  -1.255  -5.469  1.00  0.00           H
HETATM   12 2HH1 G__ A   2       3.810  -0.394  -3.955  1.00  0.00           H
HETATM   13 1HH2 G__ A   2       6.508   1.758  -4.507  1.00  0.00           H
HETATM   14 2HH2 G__ A   2       5.220   1.308  -3.415  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2
CONECT    5    6
CONECT    6    5    7   10
CONECT    7    6    8    9
CONECT    8    7   11   12
CONECT    9    7   13   14
CONECT   10    6
CONECT   11    8
CONECT   12    8
CONECT   13    9
CONECT   14    9
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "HE", "NE"),
        pick_ray(pose.residue(2), "1HH1", "NH1"),
        pick_ray(pose.residue(2), "2HH1", "NH1"),
        pick_ray(pose.residue(2), "1HH2", "NH2"),
        pick_ray(pose.residue(2), "2HH2", "NH2")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OE1", "CD"),
        pick_ray(pose.residue(1), "OE2", "CD")
    ]
}

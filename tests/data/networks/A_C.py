from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "A_C"

contents = """
HETNAM     A__ A   1  A__
HETNAM     C__ A   2  C__
HETATM    1  CV  A__ A   1       9.266  -1.353   1.889  1.00  0.00           X
HETATM    2  NZ  A__ A   1       8.868  -2.076   0.692  1.00  0.00           N
HETATM    3 1HZ  A__ A   1       8.088  -2.681   0.907  1.00  0.00           H
HETATM    4 2HZ  A__ A   1       8.596  -1.417  -0.025  1.00  0.00           H
HETATM    5 3HZ  A__ A   1       9.643  -2.633   0.359  1.00  0.00           H
HETATM    6  CV  C__ A   2       7.664  -5.462  -2.587  1.00  0.00           X
HETATM    7  CD  C__ A   2       7.954  -4.055  -2.143  1.00  0.00           C
HETATM    8  OE1 C__ A   2       8.358  -3.263  -2.964  1.00  0.00           O
HETATM    9  OE2 C__ A   2       7.772  -3.770  -0.980  1.00  0.00           O
TER
CONECT    1    2
CONECT    2    1    3    4    5
CONECT    3    2
CONECT    4    2
CONECT    5    2
CONECT    6    7
CONECT    7    6    8    9
CONECT    8    7
CONECT    9    7
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HZ", "NZ"),
        pick_ray(pose.residue(1), "2HZ", "NZ"),
        pick_ray(pose.residue(1), "3HZ", "NZ")
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OE1", "CD"),
        pick_ray(pose.residue(2), "OE2", "CD")
    ]
}

from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "C_A"

contents = """
HETNAM     C__ A   1  C__
HETNAM     A__ A   2  A__
HETATM    1  CV  C__ A   1       6.947   3.607  -1.526  1.00  0.00           X
HETATM    2  CD  C__ A   1       6.762   2.118  -1.437  1.00  0.00           C
HETATM    3  OE1 C__ A   1       6.966   1.574  -0.375  1.00  0.00           O
HETATM    4  OE2 C__ A   1       6.416   1.522  -2.433  1.00  0.00           O
HETATM    5  CV  A__ A   2       4.057   0.618  -5.697  1.00  0.00           X
HETATM    6  NZ  A__ A   2       4.561   0.062  -4.452  1.00  0.00           N
HETATM    7 1HZ  A__ A   2       4.934   0.805  -3.877  1.00  0.00           H
HETATM    8 2HZ  A__ A   2       3.808  -0.399  -3.959  1.00  0.00           H
HETATM    9 3HZ  A__ A   2       5.292  -0.607  -4.650  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2
CONECT    5    6
CONECT    6    5    7    8    9
CONECT    7    6
CONECT    8    6
CONECT    9    6
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "1HZ", "NZ"),
        pick_ray(pose.residue(2), "2HZ", "NZ"),
        pick_ray(pose.residue(2), "3HZ", "NZ")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OE1", "CD"),
        pick_ray(pose.residue(1), "OE2", "CD")
    ]
}

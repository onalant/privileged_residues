from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "C_CA"

contents = """
HETNAM     C__ A   1  C__
HETNAM     CA_ A   2  CA_
HETATM    1  CV  C__ A   1       6.947   3.607  -1.526  1.00  0.00           X
HETATM    2  CD  C__ A   1       6.762   2.118  -1.437  1.00  0.00           C
HETATM    3  OE1 C__ A   1       6.966   1.574  -0.375  1.00  0.00           O
HETATM    4  OE2 C__ A   1       6.416   1.522  -2.433  1.00  0.00           O
HETATM    5  CV  CA_ A   2       5.719   1.482  -5.949  1.00  0.00           X
HETATM    6  CG  CA_ A   2       4.669   0.476  -5.567  1.00  0.00           C
HETATM    7  OD1 CA_ A   2       4.008  -0.113  -6.435  1.00  0.00           O
HETATM    8  ND2 CA_ A   2       4.496   0.261  -4.270  1.00  0.00           N
HETATM    9 1HD2 CA_ A   2       3.808  -0.399  -3.959  1.00  0.00           H
HETATM   10 2HD2 CA_ A   2       5.049   0.755  -3.607  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2
CONECT    5    6
CONECT    6    5    7    8
CONECT    7    6
CONECT    8    6    9   10
CONECT    9    8
CONECT   10    8
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "1HD2", "ND2"),
        pick_ray(pose.residue(2), "2HD2", "ND2")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OE1", "CD"),
        pick_ray(pose.residue(1), "OE2", "CD")
    ],
    2: [
        pick_ray(pose.residue(2), "OD1", "CG")
    ]
}

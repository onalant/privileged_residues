from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "CA_C"

contents = """
HETNAM     CA_ A   1  CA_
HETNAM     C__ A   2  C__
HETATM    1  CV  CA_ A   1      11.435   0.835   1.155  1.00  0.00           X
HETATM    2  CG  CA_ A   1      10.229  -0.020   1.428  1.00  0.00           C
HETATM    3  OD1 CA_ A   1       9.811  -0.177   2.585  1.00  0.00           O
HETATM    4  ND2 CA_ A   1       9.649  -0.586   0.379  1.00  0.00           N
HETATM    5 1HD2 CA_ A   1       8.596  -1.417  -0.025  1.00  0.00           H
HETATM    6 2HD2 CA_ A   1       9.976  -0.381   0.099  1.00  0.00           H
HETATM    7  CV  C__ A   2      11.402  -3.331  -3.235  1.00  0.00           X
HETATM    8  CD  C__ A   2      10.257  -2.567  -2.631  1.00  0.00           C
HETATM    9  OE1 C__ A   2       9.130  -2.863  -2.958  1.00  0.00           O
HETATM   10  OE2 C__ A   2      10.508  -1.685  -1.841  1.00  0.00           O
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2    5    6
CONECT    5    4
CONECT    6    4
CONECT    7    8
CONECT    8    7    9   10
CONECT    9    8
CONECT   10    8
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HD2", "ND2"),
        pick_ray(pose.residue(1), "2HD2", "ND2")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OD1", "CG")
    ],
    2: [
        pick_ray(pose.residue(2), "OE1", "CD"),
        pick_ray(pose.residue(2), "OE2", "CD")
    ]
}

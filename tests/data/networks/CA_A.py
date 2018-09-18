from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "CA_A"

contents = """
HETNAM     CA_ A   1  CA_
HETNAM     A__ A   2  A__
HETATM    1  CV  CA_ A   1       9.296  -0.415  -4.208  1.00  0.00           X
HETATM    2  CG  CA_ A   1       7.841  -0.756  -4.046  1.00  0.00           C
HETATM    3  OD1 CA_ A   1       7.324  -1.665  -4.712  1.00  0.00           O
HETATM    4  ND2 CA_ A   1       7.156  -0.040  -3.165  1.00  0.00           N
HETATM    5 1HD2 CA_ A   1       6.182  -0.224  -3.018  1.00  0.00           H
HETATM    6 2HD2 CA_ A   1       7.611   0.684  -2.648  1.00  0.00           H
HETATM    7  CV  A__ A   2       4.543  -2.533  -6.739  1.00  0.00           X
HETATM    8  NZ  A__ A   2       4.494  -2.952  -5.348  1.00  0.00           N
HETATM    9 1HZ  A__ A   2       5.314  -2.612  -4.864  1.00  0.00           H
HETATM   10 2HZ  A__ A   2       3.665  -2.574  -4.910  1.00  0.00           H
HETATM   11 3HZ  A__ A   2       4.469  -3.961  -5.299  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2    5    6
CONECT    5    4
CONECT    6    4
CONECT    7    8
CONECT    8    7    9   10   11
CONECT    9    8
CONECT   10    8
CONECT   11    8
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HD2", "ND2"),
        pick_ray(pose.residue(1), "2HD2", "ND2")
    ],
    2: [
        pick_ray(pose.residue(2), "1HZ", "NZ"),
        pick_ray(pose.residue(2), "2HZ", "NZ"),
        pick_ray(pose.residue(2), "3HZ", "NZ")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OD1", "CG")
    ]
}


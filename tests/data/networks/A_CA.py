from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "A_CA"

contents = """
HETNAM     A__ A   1  A__
HETNAM     CA_ A   2  CA_
HETATM    1  CV  A__ A   1       8.094   0.365  -2.743  1.00  0.00           X
HETATM    2  NZ  A__ A   1       6.654   0.482  -2.582  1.00  0.00           N
HETATM    3 1HZ  A__ A   1       6.223   0.614  -3.486  1.00  0.00           H
HETATM    4 2HZ  A__ A   1       6.292  -0.361  -2.157  1.00  0.00           H
HETATM    5 3HZ  A__ A   1       6.443   1.273  -1.990  1.00  0.00           H
HETATM    6  CV  CA_ A   2       4.327  -0.489  -7.434  1.00  0.00           X
HETATM    7  CG  CA_ A   2       4.304  -1.010  -6.024  1.00  0.00           C
HETATM    8  OD1 CA_ A   2       4.820  -0.364  -5.100  1.00  0.00           O
HETATM    9  ND2 CA_ A   2       3.710  -2.180  -5.830  1.00  0.00           N
HETATM   10 1HD2 CA_ A   2       3.665  -2.574  -4.910  1.00  0.00           H
HETATM   11 2HD2 CA_ A   2       3.306  -2.669  -6.603  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4    5
CONECT    3    2
CONECT    4    2
CONECT    5    2
CONECT    6    7
CONECT    7    6    8    9
CONECT    8    7
CONECT    9    7   10   11
CONECT   10    9
CONECT   11    9

"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HZ", "NZ"),
        pick_ray(pose.residue(1), "2HZ", "NZ"),
        pick_ray(pose.residue(1), "3HZ", "NZ")
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

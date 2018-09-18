from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "CA_G"

contents = """
HETNAM     CA_ A   1  CA_
HETNAM     G__ A   2  G__
HETATM    1  CV  CA_ A   1       9.631  -1.201  -1.957  1.00  0.00           X
HETATM    2  CG  CA_ A   1       8.165  -1.344  -2.260  1.00  0.00           C
HETATM    3  OD1 CA_ A   1       7.783  -1.876  -3.313  1.00  0.00           O
HETATM    4  ND2 CA_ A   1       7.322  -0.876  -1.351  1.00  0.00           N
HETATM    5 1HD2 CA_ A   1       6.333  -0.944  -1.501  1.00  0.00           H
HETATM    6 2HD2 CA_ A   1       7.671  -0.455  -0.516  1.00  0.00           H
HETATM    7  CV  G__ A   2       4.561  -7.047  -4.558  1.00  0.00           X
HETATM    8  NE  G__ A   2       5.498  -5.963  -4.311  1.00  0.00           N
HETATM    9  CZ  G__ A   2       5.165  -4.657  -4.274  1.00  0.00           C
HETATM   10  NH1 G__ A   2       3.917  -4.291  -4.469  1.00  0.00           N
HETATM   11  NH2 G__ A   2       6.089  -3.750  -4.044  1.00  0.00           N
HETATM   12  HE  G__ A   2       6.468  -6.205  -4.156  1.00  0.00           H
HETATM   13 1HH1 G__ A   2       3.209  -4.993  -4.645  1.00  0.00           H
HETATM   14 2HH1 G__ A   2       3.669  -3.312  -4.441  1.00  0.00           H
HETATM   15 1HH2 G__ A   2       7.046  -4.029  -3.895  1.00  0.00           H
HETATM   16 2HH2 G__ A   2       5.838  -2.771  -4.017  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2    5    6
CONECT    5    4
CONECT    6    4
CONECT    7    8
CONECT    8    7    9   12
CONECT    9    8   10   11
CONECT   10    9   13   14
CONECT   11    9   15   16
CONECT   12    8
CONECT   13   10
CONECT   14   10
CONECT   15   11
CONECT   16   11
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HD2", "ND2"),
        pick_ray(pose.residue(1), "2HD2", "ND2")
    ],
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
        pick_ray(pose.residue(1), "OD1", "CG")
    ]
}

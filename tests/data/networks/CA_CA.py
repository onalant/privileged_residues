from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "CA_CA"

contents = """
HETNAM     CA_ A   1  CA_
HETNAM     CA_ A   2  CA_
HETATM    1  CV  CA_ A   1       9.685  -1.355  -2.175  1.00  0.00           X
HETATM    2  CG  CA_ A   1       8.206  -1.460  -2.425  1.00  0.00           C
HETATM    3  OD1 CA_ A   1       7.773  -1.981  -3.464  1.00  0.00           O
HETATM    4  ND2 CA_ A   1       7.407  -0.972  -1.487  1.00  0.00           N
HETATM    5 1HD2 CA_ A   1       6.412  -1.017  -1.601  1.00  0.00           H
HETATM    6 2HD2 CA_ A   1       7.796  -0.560  -0.664  1.00  0.00           H
HETATM    7  CV  CA_ A   2       4.204  -5.649  -5.227  1.00  0.00           X
HETATM    8  CG  CA_ A   2       5.052  -4.430  -4.992  1.00  0.00           C
HETATM    9  OD1 CA_ A   2       4.598  -3.293  -5.188  1.00  0.00           O
HETATM   10  ND2 CA_ A   2       6.291  -4.641  -4.571  1.00  0.00           N
HETATM   11 1HD2 CA_ A   2       6.901  -3.864  -4.400  1.00  0.00           H
HETATM   12 2HD2 CA_ A   2       6.617  -5.574  -4.425  1.00  0.00           H
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
CONECT   10    8   11   12
CONECT   11   10
CONECT   12   10
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HD2", "ND2"),
        pick_ray(pose.residue(1), "2HD2", "ND2")
    ],
    2: [
        pick_ray(pose.residue(2), "1HD2", "ND2"),
        pick_ray(pose.residue(2), "2HD2", "ND2")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OD1", "CG")
    ],
    2: [
        pick_ray(pose.residue(2), "OD1", "CG")
    ]
}

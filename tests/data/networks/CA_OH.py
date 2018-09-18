from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "CA_OH"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     CA_ A   1  CA_
HETATM    1  CV  CA_ A   1       7.785   3.125  -1.779  1.00  0.00           X
HETATM    2  CG  CA_ A   1       7.322   1.764  -2.217  1.00  0.00           C
HETATM    3  OD1 CA_ A   1       7.790   0.738  -1.702  1.00  0.00           O
HETATM    4  ND2 CA_ A   1       6.400   1.726  -3.170  1.00  0.00           N
HETATM    5 1HD2 CA_ A   1       6.056   0.845  -3.499  1.00  0.00           H
HETATM    6 2HD2 CA_ A   1       6.049   2.577  -3.559  1.00  0.00           H
ATOM      7  N   SER A   2       2.703  -0.078  -2.636  1.00  0.00           N
ATOM      8  CA  SER A   2       2.886   1.192  -3.327  1.00  0.00           C
ATOM      9  C   SER A   2       1.556   1.750  -3.818  1.00  0.00           C
ATOM     10  O   SER A   2       0.633   0.996  -4.127  1.00  0.00           O
ATOM     11  CB  SER A   2       3.834   1.018  -4.498  1.00  0.00           C
ATOM     12  OG  SER A   2       4.273  -0.309  -4.595  1.00  0.00           O
ATOM     13  H   SER A   2       1.939  -0.680  -2.908  1.00  0.00           H
ATOM     14  HA  SER A   2       3.320   1.908  -2.627  1.00  0.00           H
ATOM     15 1HB  SER A   2       3.330   1.306  -5.420  1.00  0.00           H
ATOM     16 2HB  SER A   2       4.691   1.679  -4.374  1.00  0.00           H
ATOM     17  HG  SER A   2       3.848  -0.782  -3.875  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2    5    6
CONECT    5    4
CONECT    6    4
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "1HD2", "ND2"),
        pick_ray(pose.residue(1), "2HD2", "ND2")
    ],
    2: [
        pick_ray(pose.residue(2), "HG", "OG")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OD1", "CG")
    ],
    2: [
        pick_ray(pose.residue(2), "OG", "CB")
    ]
}

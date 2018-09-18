from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "A_OH"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     A__ A   1  A__
HETATM    1  CV  A__ A   1       6.621   0.516  -5.419  1.00  0.00           X
HETATM    2  NZ  A__ A   1       5.837   0.332  -4.208  1.00  0.00           N
HETATM    3 1HZ  A__ A   1       4.853   0.390  -4.431  1.00  0.00           H
HETATM    4 2HZ  A__ A   1       6.038  -0.575  -3.810  1.00  0.00           H
HETATM    5 3HZ  A__ A   1       6.073   1.052  -3.539  1.00  0.00           H
ATOM      6  N   SER A   2       2.540  -1.649  -3.464  1.00  0.00           N
ATOM      7  CA  SER A   2       2.570  -0.298  -4.012  1.00  0.00           C
ATOM      8  C   SER A   2       1.166   0.285  -4.117  1.00  0.00           C
ATOM      9  O   SER A   2       0.193  -0.444  -4.304  1.00  0.00           O
ATOM     10  CB  SER A   2       3.228  -0.303  -5.378  1.00  0.00           C
ATOM     11  OG  SER A   2       3.626  -1.597  -5.739  1.00  0.00           O
ATOM     12  H   SER A   2       1.731  -2.230  -3.632  1.00  0.00           H
ATOM     13  HA  SER A   2       3.154   0.335  -3.342  1.00  0.00           H
ATOM     14 1HB  SER A   2       2.531   0.086  -6.119  1.00  0.00           H
ATOM     15 2HB  SER A   2       4.095   0.357  -5.366  1.00  0.00           H
ATOM     16  HG  SER A   2       3.372  -2.166  -5.008  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4    5
CONECT    3    2
CONECT    4    2
CONECT    5    2
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
        pick_ray(pose.residue(2), "HG", "OG")
    ]
}

sc_acceptor = {
    2: [
        pick_ray(pose.residue(2), "OG", "CB")
    ]
}

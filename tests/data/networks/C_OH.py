from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "C_OH"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     C__ A   1  C__
HETATM    1  CV  C__ A   1       8.630  -4.189  -8.071  1.00  0.00           X
HETATM    2  CD  C__ A   1       8.040  -3.267  -7.041  1.00  0.00           C
HETATM    3  OE1 C__ A   1       7.493  -3.754  -6.077  1.00  0.00           O
HETATM    4  OE2 C__ A   1       8.135  -2.072  -7.216  1.00  0.00           O
ATOM      5  N   SER A   2       7.756  -0.439  -5.359  1.00  0.00           N
ATOM      6  CA  SER A   2       7.794  -1.267  -4.159  1.00  0.00           C
ATOM      7  C   SER A   2       7.667  -0.419  -2.900  1.00  0.00           C
ATOM      8  O   SER A   2       8.086   0.738  -2.875  1.00  0.00           O
ATOM      9  CB  SER A   2       9.083  -2.064  -4.116  1.00  0.00           C
ATOM     10  OG  SER A   2       9.881  -1.788  -5.234  1.00  0.00           O
ATOM     11  H   SER A   2       8.106   0.507  -5.315  1.00  0.00           H
ATOM     12  HA  SER A   2       6.952  -1.961  -4.191  1.00  0.00           H
ATOM     13 1HB  SER A   2       9.630  -1.821  -3.206  1.00  0.00           H
ATOM     14 2HB  SER A   2       8.852  -3.128  -4.084  1.00  0.00           H
ATOM     15  HG  SER A   2       9.394  -1.147  -5.756  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    4
CONECT    3    2
CONECT    4    2
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "HG", "OG")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OE1", "CD"),
        pick_ray(pose.residue(1), "OE2", "CD")
    ],
    2: [
        pick_ray(pose.residue(2), "OG", "CB")
    ]
}

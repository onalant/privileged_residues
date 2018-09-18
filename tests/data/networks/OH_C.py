from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "OH_C"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     C__ A   2  C__
ATOM      1  N   SER A   1       7.651  -1.446  -7.065  1.00  0.00           N
ATOM      2  CA  SER A   1       6.744  -1.758  -5.967  1.00  0.00           C
ATOM      3  C   SER A   1       7.027  -0.881  -4.753  1.00  0.00           C
ATOM      4  O   SER A   1       8.163  -0.465  -4.528  1.00  0.00           O
ATOM      5  CB  SER A   1       6.869  -3.220  -5.586  1.00  0.00           C
ATOM      6  OG  SER A   1       7.817  -3.869  -6.389  1.00  0.00           O
ATOM      7  H   SER A   1       8.579  -1.106  -6.856  1.00  0.00           H
ATOM      8  HA  SER A   1       5.722  -1.566  -6.297  1.00  0.00           H
ATOM      9 1HB  SER A   1       7.160  -3.300  -4.539  1.00  0.00           H
ATOM     10 2HB  SER A   1       5.901  -3.708  -5.694  1.00  0.00           H
ATOM     11  HG  SER A   1       8.154  -3.202  -6.992  1.00  0.00           H
HETATM   12  CV  C__ A   2      11.812  -3.864  -4.817  1.00  0.00           X
HETATM   13  CD  C__ A   2      10.413  -3.317  -4.875  1.00  0.00           C
HETATM   14  OE1 C__ A   2       9.701  -3.452  -3.906  1.00  0.00           O
HETATM   15  OE2 C__ A   2      10.054  -2.763  -5.890  1.00  0.00           O
TER
CONECT   12   13
CONECT   13   12   14   15
CONECT   14   13
CONECT   15   13
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HG", "OG")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OG", "CB")
    ],
    2: [
        pick_ray(pose.residue(2), "OE1", "CD"),
        pick_ray(pose.residue(2), "OE2", "CD")
    ]
}

from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "OH_A"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     A__ A   2  A__
ATOM      1  N   SER A   1       4.933  -1.401  -2.728  1.00  0.00           N
ATOM      2  CA  SER A   1       4.476  -0.018  -2.794  1.00  0.00           C
ATOM      3  C   SER A   1       3.035   0.064  -3.280  1.00  0.00           C
ATOM      4  O   SER A   1       2.580  -0.783  -4.050  1.00  0.00           O
ATOM      5  CB  SER A   1       5.376   0.785  -3.714  1.00  0.00           C
ATOM      6  OG  SER A   1       6.394  -0.017  -4.246  1.00  0.00           O
ATOM      7  H   SER A   1       4.546  -2.078  -3.370  1.00  0.00           H
ATOM      8  HA  SER A   1       4.525   0.411  -1.793  1.00  0.00           H
ATOM      9 1HB  SER A   1       4.783   1.209  -4.524  1.00  0.00           H
ATOM     10 2HB  SER A   1       5.814   1.615  -3.161  1.00  0.00           H
ATOM     11  HG  SER A   1       6.258  -0.895  -3.881  1.00  0.00           H
HETATM   12  CV  A__ A   2       3.512  -1.512  -7.034  1.00  0.00           X
HETATM   13  NZ  A__ A   2       4.049  -1.531  -5.683  1.00  0.00           N
HETATM   14 1HZ  A__ A   2       4.411  -0.616  -5.451  1.00  0.00           H
HETATM   15 2HZ  A__ A   2       3.316  -1.777  -5.031  1.00  0.00           H
HETATM   16 3HZ  A__ A   2       4.794  -2.211  -5.622  1.00  0.00           H
TER
CONECT   12   13
CONECT   13   12   14   15   16
CONECT   14   13
CONECT   15   13
CONECT   16   13
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HG", "OG")
    ],
    2: [
        pick_ray(pose.residue(2), "1HZ", "NZ"),
        pick_ray(pose.residue(2), "2HZ", "NZ"),
        pick_ray(pose.residue(2), "3HZ", "NZ")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OG", "CB")
    ]
}

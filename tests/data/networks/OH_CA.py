from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "OH_CA"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     CA_ A   2  CA_
ATOM      1  N   SER A   1       7.325  -0.564  -0.880  1.00  0.00           N
ATOM      2  CA  SER A   1       6.685  -1.205   0.262  1.00  0.00           C
ATOM      3  C   SER A   1       5.988  -0.180   1.149  1.00  0.00           C
ATOM      4  O   SER A   1       6.413   0.972   1.234  1.00  0.00           O
ATOM      5  CB  SER A   1       7.710  -1.974   1.072  1.00  0.00           C
ATOM      6  OG  SER A   1       8.986  -1.860   0.505  1.00  0.00           O
ATOM      7  H   SER A   1       7.667   0.381  -0.786  1.00  0.00           H
ATOM      8  HA  SER A   1       5.933  -1.903  -0.109  1.00  0.00           H
ATOM      9 1HB  SER A   1       7.728  -1.593   2.093  1.00  0.00           H
ATOM     10 2HB  SER A   1       7.423  -3.023   1.120  1.00  0.00           H
ATOM     11  HG  SER A   1       8.881  -1.308  -0.274  1.00  0.00           H
HETATM   12  CV  CA_ A   2       8.703  -5.200  -3.411  1.00  0.00           X
HETATM   13  CG  CA_ A   2       8.464  -3.979  -2.567  1.00  0.00           C
HETATM   14  OD1 CA_ A   2       8.766  -2.851  -2.983  1.00  0.00           O
HETATM   15  ND2 CA_ A   2       7.921  -4.176  -1.373  1.00  0.00           N
HETATM   16 1HD2 CA_ A   2       7.740  -3.398  -0.770  1.00  0.00           H
HETATM   17 2HD2 CA_ A   2       7.692  -5.102  -1.076  1.00  0.00           H
TER
CONECT   12   13
CONECT   13   12   14   15
CONECT   14   13
CONECT   15   13   16   17
CONECT   16   15
CONECT   17   15
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HG", "OG")
    ],
    2: [
        pick_ray(pose.residue(2), "1HD2", "ND2"),
        pick_ray(pose.residue(2), "2HD2", "ND2")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OG", "CB")
    ],
    2: [
        pick_ray(pose.residue(2), "OD1", "CG")
    ]
}

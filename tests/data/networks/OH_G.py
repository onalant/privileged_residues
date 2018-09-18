from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "OH_G"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     G__ A   2  G__
ATOM      1  N   SER A   1       4.933  -1.394  -2.636  1.00  0.00           N
ATOM      2  CA  SER A   1       4.464  -0.115  -2.115  1.00  0.00           C
ATOM      3  C   SER A   1       3.120   0.267  -2.721  1.00  0.00           C
ATOM      4  O   SER A   1       2.815  -0.095  -3.857  1.00  0.00           O
ATOM      5  CB  SER A   1       5.484   0.970  -2.398  1.00  0.00           C
ATOM      6  OG  SER A   1       6.593   0.451  -3.080  1.00  0.00           O
ATOM      7  H   SER A   1       4.671  -1.669  -3.572  1.00  0.00           H
ATOM      8  HA  SER A   1       4.339  -0.207  -1.035  1.00  0.00           H
ATOM      9 1HB  SER A   1       5.022   1.756  -2.994  1.00  0.00           H
ATOM     10 2HB  SER A   1       5.808   1.419  -1.460  1.00  0.00           H
ATOM     11  HG  SER A   1       6.418  -0.485  -3.196  1.00  0.00           H
HETATM   12  CV  G__ A   2       6.228  -0.877  -7.450  1.00  0.00           X
HETATM   13  NE  G__ A   2       5.778   0.033  -6.408  1.00  0.00           N
HETATM   14  CZ  G__ A   2       4.710  -0.181  -5.613  1.00  0.00           C
HETATM   15  NH1 G__ A   2       3.995  -1.275  -5.753  1.00  0.00           N
HETATM   16  NH2 G__ A   2       4.383   0.706  -4.698  1.00  0.00           N
HETATM   17  HE  G__ A   2       6.303   0.886  -6.270  1.00  0.00           H
HETATM   18 1HH1 G__ A   2       4.250  -1.955  -6.459  1.00  0.00           H
HETATM   19 2HH1 G__ A   2       3.195  -1.435  -5.157  1.00  0.00           H
HETATM   20 1HH2 G__ A   2       4.931   1.546  -4.589  1.00  0.00           H
HETATM   21 2HH2 G__ A   2       3.583   0.544  -4.103  1.00  0.00           H
TER
CONECT   12   13
CONECT   13   12   14   17
CONECT   14   13   15   16
CONECT   15   14   18   19
CONECT   16   14   20   21
CONECT   17   13
CONECT   18   15
CONECT   19   15
CONECT   20   16
CONECT   21   16
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HG", "OG")
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
        pick_ray(pose.residue(1), "OG", "CB")
    ]
}

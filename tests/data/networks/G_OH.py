from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "G_OH"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
HETNAM     G__ A   1  G__
HETATM    1  CV  G__ A   1       7.418  -1.263  -7.810  1.00  0.00           X
HETATM    2  NE  G__ A   1       6.975  -2.451  -7.097  1.00  0.00           N
HETATM    3  CZ  G__ A   1       6.446  -2.447  -5.857  1.00  0.00           C
HETATM    4  NH1 G__ A   1       6.301  -1.312  -5.208  1.00  0.00           N
HETATM    5  NH2 G__ A   1       6.076  -3.577  -5.296  1.00  0.00           N
HETATM    6  HE  G__ A   1       7.071  -3.343  -7.564  1.00  0.00           H
HETATM    7 1HH1 G__ A   1       6.587  -0.444  -5.644  1.00  0.00           H
HETATM    8 2HH1 G__ A   1       5.905  -1.309  -4.279  1.00  0.00           H
HETATM    9 1HH2 G__ A   1       6.186  -4.448  -5.791  1.00  0.00           H
HETATM   10 2HH2 G__ A   1       5.680  -3.572  -4.366  1.00  0.00           H
ATOM     11  N   SER A   2       1.978  -2.642  -3.670  1.00  0.00           N
ATOM     12  CA  SER A   2       1.896  -3.244  -4.995  1.00  0.00           C
ATOM     13  C   SER A   2       0.553  -3.931  -5.207  1.00  0.00           C
ATOM     14  O   SER A   2      -0.060  -4.420  -4.258  1.00  0.00           O
ATOM     15  CB  SER A   2       3.021  -4.243  -5.185  1.00  0.00           C
ATOM     16  OG  SER A   2       3.827  -4.315  -4.041  1.00  0.00           O
ATOM     17  H   SER A   2       1.466  -3.062  -2.907  1.00  0.00           H
ATOM     18  HA  SER A   2       1.998  -2.454  -5.741  1.00  0.00           H
ATOM     19 1HB  SER A   2       2.602  -5.226  -5.400  1.00  0.00           H
ATOM     20 2HB  SER A   2       3.626  -3.951  -6.042  1.00  0.00           H
ATOM     21  HG  SER A   2       3.450  -3.695  -3.412  1.00  0.00           H
TER
CONECT    1    2
CONECT    2    1    3    6
CONECT    3    2    4    5
CONECT    4    3    7    8
CONECT    5    3    9   10
CONECT    6    2
CONECT    7    4
CONECT    8    4
CONECT    9    5
CONECT   10    5
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HE", "NE"),
        pick_ray(pose.residue(1), "1HH1", "NH1"),
        pick_ray(pose.residue(1), "2HH1", "NH1"),
        pick_ray(pose.residue(1), "1HH2", "NH2"),
        pick_ray(pose.residue(1), "2HH2", "NH2")
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

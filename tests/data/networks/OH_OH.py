from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "OH_OH"

# NOTE(onalant): serines substituted for hydroxyls since we need real carbons
contents = """
ATOM      1  N   SER A   1       7.975  -0.175  -0.127  1.00  0.00           N
ATOM      2  CA  SER A   1       9.177   0.631   0.051  1.00  0.00           C
ATOM      3  C   SER A   1       9.173   1.839  -0.877  1.00  0.00           C
ATOM      4  O   SER A   1       8.606   1.793  -1.969  1.00  0.00           O
ATOM      5  CB  SER A   1      10.412  -0.211  -0.206  1.00  0.00           C
ATOM      6  OG  SER A   1      10.063  -1.526  -0.542  1.00  0.00           O
ATOM      7  H   SER A   1       7.528  -0.198  -1.033  1.00  0.00           H
ATOM      8  HA  SER A   1       9.204   0.990   1.080  1.00  0.00           H
ATOM      9 1HB  SER A   1      10.993   0.232  -1.015  1.00  0.00           H
ATOM     10 2HB  SER A   1      11.040  -0.215   0.684  1.00  0.00           H
ATOM     11  HG  SER A   1       9.103  -1.558  -0.523  1.00  0.00           H
ATOM     12  N   SER A   2       9.807  -1.298  -0.973  1.00  0.00           N
ATOM     13  CA  SER A   2       8.484  -1.352  -1.582  1.00  0.00           C
ATOM     14  C   SER A   2       7.533  -2.211  -0.759  1.00  0.00           C
ATOM     15  O   SER A   2       7.953  -3.156  -0.093  1.00  0.00           O
ATOM     16  CB  SER A   2       8.581  -1.899  -2.993  1.00  0.00           C
ATOM     17  OG  SER A   2       9.908  -2.202  -3.324  1.00  0.00           O
ATOM     18  H   SER A   2      10.132  -2.087  -0.431  1.00  0.00           H
ATOM     19  HA  SER A   2       8.081  -0.339  -1.625  1.00  0.00           H
ATOM     20 1HB  SER A   2       7.968  -2.796  -3.078  1.00  0.00           H
ATOM     21 2HB  SER A   2       8.187  -1.166  -3.695  1.00  0.00           H
ATOM     22  HG  SER A   2      10.432  -1.979  -2.550  1.00  0.00           H
TER
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

sc_donor = {
    1: [
        pick_ray(pose.residue(1), "HG", "OG")
    ],
    2: [
        pick_ray(pose.residue(2), "HG", "OG")
    ]
}

sc_acceptor = {
    1: [
        pick_ray(pose.residue(1), "OG", "CB")
    ],
    2: [
        pick_ray(pose.residue(2), "OG", "CB")
    ]
}

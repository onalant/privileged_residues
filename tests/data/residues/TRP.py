from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "TRP"

contents = """
ATOM      1  N   ALA A   1       0.000   0.000   0.000  1.00  0.00           N
ATOM      2  CA  ALA A   1       1.458   0.000   0.000  1.00  0.00           C
ATOM      3  C   ALA A   1       2.009   1.420   0.000  1.00  0.00           C
ATOM      4  O   ALA A   1       1.251   2.390   0.000  1.00  0.00           O
ATOM      5  CB  ALA A   1       1.988  -0.773  -1.199  1.00  0.00           C
ATOM      6 1H   ALA A   1      -0.334  -0.943  -0.000  1.00  0.00           H
ATOM      7 2H   ALA A   1      -0.334   0.471   0.816  1.00  0.00           H
ATOM      8 3H   ALA A   1      -0.334   0.471  -0.816  1.00  0.00           H
ATOM      9  HA  ALA A   1       1.797  -0.490   0.913  1.00  0.00           H
ATOM     10 1HB  ALA A   1       3.078  -0.764  -1.185  1.00  0.00           H
ATOM     11 2HB  ALA A   1       1.633  -1.802  -1.154  1.00  0.00           H
ATOM     12 3HB  ALA A   1       1.633  -0.307  -2.117  1.00  0.00           H
ATOM     13  N   TRP A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  TRP A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   TRP A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   TRP A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  TRP A   2       3.550   3.655   1.217  1.00  0.00           C
ATOM     18  CG  TRP A   2       2.574   2.938   2.100  1.00  0.00           C
ATOM     19  CD1 TRP A   2       2.074   1.684   1.913  1.00  0.00           C
ATOM     20  CD2 TRP A   2       1.973   3.431   3.322  1.00  0.00           C
ATOM     21  NE1 TRP A   2       1.206   1.365   2.927  1.00  0.00           N
ATOM     22  CE2 TRP A   2       1.133   2.421   3.799  1.00  0.00           C
ATOM     23  CE3 TRP A   2       2.078   4.630   4.037  1.00  0.00           C
ATOM     24  CZ2 TRP A   2       0.396   2.570   4.963  1.00  0.00           C
ATOM     25  CZ3 TRP A   2       1.340   4.778   5.205  1.00  0.00           C
ATOM     26  CH2 TRP A   2       0.521   3.774   5.656  1.00  0.00           C
ATOM     27  H   TRP A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     28  HA  TRP A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     29 1HB  TRP A   2       4.425   3.916   1.814  1.00  0.00           H
ATOM     30 2HB  TRP A   2       3.092   4.586   0.885  1.00  0.00           H
ATOM     31  HD1 TRP A   2       2.327   1.031   1.079  1.00  0.00           H
ATOM     32  HE1 TRP A   2       0.702   0.494   3.017  1.00  0.00           H
ATOM     33  HE3 TRP A   2       2.729   5.430   3.685  1.00  0.00           H
ATOM     34  HZ2 TRP A   2      -0.261   1.784   5.337  1.00  0.00           H
ATOM     35  HZ3 TRP A   2       1.427   5.715   5.756  1.00  0.00           H
ATOM     36  HH2 TRP A   2      -0.044   3.923   6.577  1.00  0.00           H
ATOM     37  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     38  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     39  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     40  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     41  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     42  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     43  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     44  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     45 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     46 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     47 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
TER
"""

pose = Pose()
pose_from_pdbstring(pose, contents)

n_rays = {
    1: pick_ray(pose.residue(1), "1H", "N"),
    2: pick_ray(pose.residue(2), "H", "N"),
    3: pick_ray(pose.residue(3), "H", "N")
}

c_rays = {
    1: pick_ray(pose.residue(1), "O", "C"),
    2: pick_ray(pose.residue(2), "O", "C"),
    3: pick_ray(pose.residue(3), "O", "C")
}

sc_donor = {
    2: [
        pick_ray(pose.residue(2), "HE1", "NE1")
    ]
}

sc_acceptor = { }

cat_pi = [
    (pick_ray(pose.residue(2), "NE1", "CG"), pick_ray(pose.residue(2), "CZ2", "CG"))
]

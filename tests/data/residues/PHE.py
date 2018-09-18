from tests.util import pick_ray

from pyrosetta import Pose
from pyrosetta.rosetta.core.import_pose import pose_from_pdbstring

name = "PHE"

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
ATOM     13  N   PHE A   2       3.332   1.536   0.000  1.00  0.00           N
ATOM     14  CA  PHE A   2       3.988   2.839   0.000  1.00  0.00           C
ATOM     15  C   PHE A   2       5.504   2.693   0.000  1.00  0.00           C
ATOM     16  O   PHE A   2       6.030   1.580   0.000  1.00  0.00           O
ATOM     17  CB  PHE A   2       3.549   3.657   1.216  1.00  0.00           C
ATOM     18  CG  PHE A   2       2.569   2.945   2.104  1.00  0.00           C
ATOM     19  CD1 PHE A   2       2.138   1.663   1.798  1.00  0.00           C
ATOM     20  CD2 PHE A   2       2.076   3.556   3.247  1.00  0.00           C
ATOM     21  CE1 PHE A   2       1.237   1.007   2.615  1.00  0.00           C
ATOM     22  CE2 PHE A   2       1.176   2.902   4.066  1.00  0.00           C
ATOM     23  CZ  PHE A   2       0.756   1.626   3.749  1.00  0.00           C
ATOM     24  H   PHE A   2       3.899   0.700   0.000  1.00  0.00           H
ATOM     25  HA  PHE A   2       3.702   3.361  -0.913  1.00  0.00           H
ATOM     26 1HB  PHE A   2       4.422   3.918   1.812  1.00  0.00           H
ATOM     27 2HB  PHE A   2       3.091   4.587   0.882  1.00  0.00           H
ATOM     28  HD1 PHE A   2       2.520   1.173   0.902  1.00  0.00           H
ATOM     29  HD2 PHE A   2       2.408   4.564   3.497  1.00  0.00           H
ATOM     30  HE1 PHE A   2       0.907  -0.000   2.363  1.00  0.00           H
ATOM     31  HE2 PHE A   2       0.796   3.394   4.962  1.00  0.00           H
ATOM     32  HZ  PHE A   2       0.045   1.110   4.393  1.00  0.00           H
ATOM     33  N   ALA A   3       6.202   3.823   0.000  1.00  0.00           N
ATOM     34  CA  ALA A   3       7.660   3.823   0.000  1.00  0.00           C
ATOM     35  C   ALA A   3       8.211   5.243   0.000  1.00  0.00           C
ATOM     36  O   ALA A   3       8.260   5.868   1.023  1.00  0.00           O
ATOM     37  OXT ALA A   3       8.596   5.737  -1.023  1.00  0.00           O
ATOM     38  CB  ALA A   3       8.190   3.050  -1.199  1.00  0.00           C
ATOM     39  H   ALA A   3       5.710   4.705  -0.000  1.00  0.00           H
ATOM     40  HA  ALA A   3       7.999   3.333   0.913  1.00  0.00           H
ATOM     41 1HB  ALA A   3       9.280   3.059  -1.185  1.00  0.00           H
ATOM     42 2HB  ALA A   3       7.835   2.021  -1.154  1.00  0.00           H
ATOM     43 3HB  ALA A   3       7.835   3.516  -2.117  1.00  0.00           H
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

sc_donor = { }

sc_acceptor = { }

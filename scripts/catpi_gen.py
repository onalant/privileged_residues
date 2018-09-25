import multiprocessing
import numpy as np
import pyrosetta
import re
import sys

from itertools import permutations

from rif.eigen_types import X3
from rif.geom.ray_hash import RayToRay4dHash
from rif.hash import XformHash_bt24_BCC6_X3f

# NOTE(onalant): change below to desired ray pair provider
from privileged_residues.chemical import catpi
from privileged_residues.geometry import coords_to_transform, create_ray
from privileged_residues.util import models_from_pdb, numpy_to_rif

dt = [("hash", "u8"), ("residue", "S3"), ("transform", "u8")]

attr = [("cart_resl", 0.1),
        ("ori_resl", 2.0),
        ("cart_bound", 16.0)]
attr = dict(attr)

cart_resl = attr["cart_resl"]
ori_resl = attr["ori_resl"]
cart_bound = attr["cart_bound"]

select = pyrosetta.rosetta.core.select.residue_selector.TrueResidueSelector()
lattice = XformHash_bt24_BCC6_X3f(cart_resl, ori_resl, cart_bound)
# WARN(onalant): constants recommended by Will Sheffler; do not change unless /absolutely/ sure
LEVER = 10
BOUND = 1000
raygrid = RayToRay4dHash(ori_resl, LEVER, bound=BOUND)

# NOTE(onalant): change as necessary
target_pair = (2, 5)
assert(2 == len(target_pair))

# WARN(onalant): What follow are fast-and-loose methods to process PDBs into
#                records. Beware of changing.
def atom_records_from_pdb(f):
    records = []
    for line in open(f):
        if (not line.startswith("ENDMDL")):
            if (line.startswith("ATOM")):
                sys.stdout.flush()
                records.append(line.strip().split())
        else:
            yield records
            records = []

    if (any(records)):
        return records

def records_to_coords(records):
    return np.array(list(map(lambda r: r[6:9], records)), dtype=np.float)

def fxnl_grp(records):
    return list(filter(lambda r: r[2] in catpi.rsd_to_fxnl_grp[records[0][3]].atoms, records))

def to_raypair(xyzs):
    ray1 = create_ray(xyzs[1], xyzs[0])
    ray2 = create_ray(xyzs[2], xyzs[0])

    return (ray1, ray2)

def write_records_from_structure(pipe, posefile):
    prefix = "[WORKER-%s]" % (re.match(".*?(\d+)", multiprocessing.current_process().name).group(1))
    print(prefix, posefile)
    for rs in atom_records_from_pdb(posefile):
        for (a, b) in permutations(target_pair):
            rA = list(filter(lambda r: r[5] == str(a), rs))
            rB = list(filter(lambda r: r[5] == str(b), rs))

            xyzA = records_to_coords(fxnl_grp(rA))
            xyzB = records_to_coords(fxnl_grp(rB))

            rpair = to_raypair(xyzA)

            hashed_rays = raygrid.get_keys(*(numpy_to_rif(r) for r in rpair)).item()

            fxBName = catpi.rsd_to_fxnl_grp[rB[0][3]].grp

            xfA = coords_to_transform(xyzA)
            xfB = coords_to_transform(xyzB)
            xfrel = xfB @ np.linalg.inv(xfA)

            transform = lattice.get_key(xfrel.astype("f4").flatten().view(X3)).item()

            record = np.array([(hashed_rays, fxBName, transform)], dtype=dt)

            pipe.put(record)


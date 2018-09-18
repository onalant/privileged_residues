import glob
import numpy as np
import os
import sys
import zarr

sys.path.append("../")

from catpi_gen import attr, dt, write_records_from_structure
from privileged_residues.dtable import gentable

from functools import partial
from multiprocessing.pool import Pool

SLURM_NCPU_NODE = "SLURM_JOB_CPUS_PER_NODE"
SLURM_NNODE = "SLURM_NNODES"

ncpu = int(os.environ[SLURM_NCPU_NODE]) * int(os.environ[SLURM_NNODE]) - 2
pool = Pool(ncpu)

name = sys.argv[1]
structures_glob = sys.argv[2]
outpath = sys.argv[3]

ndt = np.dtype(dt)

with gentable(outpath, ndt, ["hash", "residue"], name=name) as q:
    record_pipe = partial(write_records_from_structure, q)

    files = glob.iglob(structures_glob)
    pool.map(record_pipe, files)

for store in glob.glob(os.path.join(outpath, "*.zarr")):
    z = zarr.open(store)
    if (z.attrs["name"] == name):
        z.attrs.update(attr)

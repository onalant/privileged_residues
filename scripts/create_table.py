import glob
import numpy as np
import os
import sys
import zarr

sys.path.append("../")
sys.path.append("/home/onalant/source/")

from generators.catpi import attr, dt, preprocess, write_records
from dtable import gentable

from functools import partial
from multiprocessing.pool import Pool
from os import path

SLURM_NCPU_NODE = "SLURM_JOB_CPUS_PER_NODE"
SLURM_NNODE = "SLURM_NNODES"

ncpu = int(os.environ[SLURM_NCPU_NODE]) * int(os.environ[SLURM_NNODE]) - 2
pool = Pool(ncpu)

name = sys.argv[1]
globexpr = path.join(sys.argv[2], "*.pdb")
outpath = sys.argv[3]

ndt = np.dtype(dt)

with gentable(outpath, ndt, [*ndt.names[:2]], name=name) as q:
    record_pipe = partial(write_records, q)

    files = glob.iglob(globexpr)
    data = preprocess(files)
    pool.map(record_pipe, data)

for store in glob.glob(os.path.join(outpath, "*.zarr")):
    z = zarr.open(store)
    if ("name" in z.attrs and z.attrs["name"] == name):
        z.attrs.update(attr)

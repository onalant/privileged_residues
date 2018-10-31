import numpy as np
import os
import zarr

from itertools import product

from rif.eigen_types import X3
from rif.hash import XformHash_bt24_BCC6_X3f

from xbin import XformBinner

dt = np.dtype([("hash", "u8"), ("residue", "S3"), ("transform", "u8")])

attr = [("cart_resl", 0.1),
        ("ori_resl", 2.0),
        ("cart_bound", 16.0)]
attr = dict(attr)

cart_resl = attr["cart_resl"]
ori_resl = attr["ori_resl"]
cart_bound = attr["cart_bound"]

oldlat = XformHash_bt24_BCC6_X3f(cart_resl, ori_resl, cart_bound)
newlat = XformBinner(cart_resl, ori_resl, cart_bound)

SLURM_NCPU_NODE = "SLURM_JOB_CPUS_PER_NODE"
SLURM_NNODE = "SLURM_NNODES"

ncpu = int(os.environ[SLURM_NCPU_NODE]) * int(os.environ[SLURM_NNODE]) - 2

def Rekey(RecordProcessor):
    def preprocess(zarrfiles):
        partitions = [ ]

        for zarrfile in zarrfiles:
            tbl = zarr.open(zarrfile, mode="r")

            chunks = [min(p // ncpu, q) for (p, q) in zip(tbl.shape, tbl.chunks)]
            raw_parts = tuple(np.mgrid[0:p:q] for (p, q) in zip(tbl.shape, chunks))

            for partition in product(*raw_parts):
                partitions.append((zarrfile, tuple(np.s_[p:p+q] for (p, q) in zip(partition, chunks))))

        return partitions

    def write_records(pipe, tbl_segment):
        (zarrfile, partition) = tbl_segment

        self.log(zarrfile, *("%d:%d" % (axis.start, axis.stop) + (":%d" % (axis.step) if axis.step is not None else "") for axis in partition))

        tbl = zarr.open(zarrfile, mode="r")

        for record in tbl[partition]:
            try:
                dummy = newlat.get_bin_index(oldlat.get_center([record["transform"]])["raw"].squeeze())
            except:
                t = datetime.now().time().isoformat(timespec="milliseconds")
                self.log(record)
                continue
            record["transform"] = dummy

            pipe.put(record)

import dask.array as da
import multiprocessing
import numpy as np
import os
import random
import sys
import threading
import zarr

from collections import namedtuple
from contextlib import contextmanager
from numcodecs.blosc import Blosc
from os import path

FinishSignal = namedtuple("FinishSignal", [])

def writer(q, outfile, dtype, intermediate, dimensions):
	disk = zarr.open(outfile, shape=(0,), chunks=(intermediate,), dtype=dtype, mode="w", fill_value=None, compressor=Blosc(cname="lz4", clevel=5, shuffle=2))

	def _dump_to_disk(buffer):
		buffer = np.sort(buffer, dimensions.reverse(), kind="heapsort")
		dset = disk.append(buffer)

	buffer = np.empty(intermediate, dtype=dtype)
	record = q.get()
	cur = 0

	while (not isinstance(record, FinishSignal)):
		buffer[cur] = record
		cur += 1

		if (intermediate and cur >= intermediate): # if intermediate is 0, then just dump at the end
			_dump_to_disk(buffer)
			cur = 0

		record = q.get()

	if (cur > 0):
		_dump_to_disk(buffer[:cur])

@contextmanager
def gentable(outdir, dtype, dimensions, chunk_mib = 100, loadfactor = 5, name = "default"):
	outdir = path.expanduser(outdir)
	fname = hex(random.getrandbits(64))[2:].upper()

	outfile = path.join(outdir, "%s.zarr" % (fname))

	os.makedirs(outdir, exist_ok=True)

	intermediate = chunk_mib * 1000 ** 2 // dtype.itemsize

	m = multiprocessing.Manager()
	q = m.Queue(intermediate * loadfactor)

	worker = threading.Thread(target=writer, args=[q, outfile, dtype, intermediate, dimensions], daemon=True)
	worker.start()

	try:
		yield q
	finally:
		q.put(FinishSignal())
		worker.join()

		final = zarr.open(outfile)
		final.attrs["name"] = name


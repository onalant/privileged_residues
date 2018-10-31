import multiprocessing
import numpy as np
import os
import re
import zarr

from datetime import datetime
from itertools import product

prefix = "[WORKER-%s]" % (re.match(".*?(\d+)", multiprocessing.current_process().name).group(1))

class RecordProcessor:
    def log(*message):
        t = datetime.now().time().isoformat(timespec="milliseconds")
        print(t, prefix, *message)

    def preprocess(files):
        return files

    def write_records(pipe, tbl_segment):
        raise NotImplementedError("Implement the record writer!")

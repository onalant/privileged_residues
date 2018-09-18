import dask
import dask.array as da
import dask.bag as db
import glob
import numpy as np
import os
import zarr

from functools import reduce
from os import path

class Table:
    @staticmethod
    def from_multifile(globexpr):
        files = glob.glob(path.expanduser(globexpr))
        
        arrays = [ ]
        attrs = { }

        for file in files:
            dstore = zarr.open(file, mode="r")

            tmp = da.from_zarr(dstore)
            name = dstore.attrs["name"]
            array = da.from_array(tmp, chunks=tmp.chunksize, name=name)

            arrays.append(array)
            attrs[name] = dstore.attrs

        return Table(arrays, attrs)

    def __init__(self, arrays, attrs = { }):
        self.attrs = attrs
        self._data = db.from_sequence(arrays, npartitions=1)
        
    def __getitem__(self, key):
        """
        Parameters
        ----------
        key : string
            Array label.

        Returns
        -------
        dask.array.Array
            Subarray of table matching supplied label.
        """

        return self._data.filter(lambda subset: subset.name == key).compute()
                
    def __iter__(self):
        """
        Yields
        ------
        np.ndarray
            A record from the database.
        """

        pass

    def __len__(self):
        """
        Returns
        -------
        int
            The total number of records in the database.
        """

        return self._data.map(lambda p: len(p)).fold(sum).compute()

    def fetch(self, **params):
        return self._data.filter(lambda p: p.name in params) \
            .map(lambda p: p[ \
                reduce( \
                    lambda x, y: np.bitwise_and(x, (p[y[0]] == y[1])), \
                    params[p.name].items(), \
                    np.ones(p.shape, dtype=bool) \
                ) \
            ]) \
            .fold(lambda p, q: da.concatenate([p, q])) \
            .apply(lambda p: da.unique(p.compute())) \
            .compute()
        

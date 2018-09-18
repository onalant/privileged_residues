import pytest

import numpy as np

from privileged_residues import geometry

from numpy.testing import assert_allclose

c = np.identity(3)
d = np.zeros(3)

@pytest.mark.parametrize("coords", [
    (c),
    pytest.param(
        d,
        marks=[
            pytest.mark.filterwarnings("ignore::RuntimeWarning"),
            pytest.mark.xfail(reason="edge-case where computed axes "
                                     "are parallel")
        ]
    )
], ids=["ideal", "degenerate"])
def test(coords):
    trans = geometry.coords_to_transform(coords)

    assert_allclose(np.linalg.det(trans[:3, :3]), 1.0)
    assert_allclose(trans[:3, 3], coords[2])


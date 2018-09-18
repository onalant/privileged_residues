import pytest

import numpy as np

from privileged_residues import geometry

from numpy.testing import assert_allclose

c = geometry.create_ray(np.zeros(3), -np.ones(3))
d = geometry.create_ray(np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))

@pytest.mark.parametrize("a,b", [
    (c, d),
    pytest.param(
        c, c,
        marks=[
            pytest.mark.filterwarnings("ignore::RuntimeWarning"),
            pytest.mark.xfail(reason="edge-case where computed axes "
                                     "are parallel")
        ]
    )
], ids=["ideal", "degenerate"])
def test(a, b):
    trans = geometry.rays_to_transform(a, b)

    assert_allclose(np.linalg.det(trans[:3, :3]), 1.0)
    assert_allclose(trans[:3, 3], a[:3, 0])


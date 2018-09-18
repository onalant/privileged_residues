import pytest

import numpy as np

from privileged_residues import geometry

from numpy.testing import assert_allclose

@pytest.mark.parametrize("component", [
    (1.0),
    pytest.param(
        1e-160,
        marks=[
            pytest.mark.filterwarnings("ignore::RuntimeWarning"),
            pytest.mark.xfail(reason="edge-case where ray is too short "
                                     "to normalize properly")
        ]
    )
], ids=["ideal", "degenerate"])
def test(component):
    center = np.full(3, component)
    base = np.zeros(3)

    ray = geometry.create_ray(center, base)

    direction = center - base

    assert_allclose(np.linalg.norm(ray[:-1, 1]), 1.0)
    assert_allclose(np.cross(direction, ray[:-1, 1]), 0.0)
    assert_allclose(ray[:-1, 0], center)


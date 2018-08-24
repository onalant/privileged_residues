import pytest

import numpy as np

from privileged_residues import geometry

from numpy.testing import assert_allclose

class TestRayCreation:
    def test_ideal(self):
        center = np.full(3, 1.0)
        base = np.full(3, 0.0)

        ray = geometry.create_ray(center, base)

        direction = center - base

        assert_allclose(np.cross(direction, ray[:-1, 1]), 0.0)
        assert_allclose(ray[:-1, 0], center)

    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    @pytest.mark.xfail(reason="edge-case where ray is too short to "
                              "normalize properly") # (strict=True)
    def test_degenerate(self):
        center = np.full(3)
        base = np.full(3, 1.1111111111111111e-160)

        geometry.create_ray(center, base)

class TestRayTransform:
    def test_ideal(self):
        a = geometry.create_ray(np.full(3, 0.0), np.full(3, 1.0))
        b = geometry.create_ray(np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]))

        xform = geometry.rays_to_transform(a, b)

        assert_allclose(xform[:-1, 3], [0] * 3)

    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    @pytest.mark.xfail(reason="edge-case where computed axes are"
                              "parallel") # (strict=True)
    def test_degenerate(self):
        a = geometry.create_ray(np.full(3, 0.0), np.full(3, 1.0))
        b = geometry.create_ray(np.full(3, 1.0), np.array([0.0, 1.0, 0.0]))

        geometry.rays_to_transform(a, b)

class TestCoordTransform:
    def test_ideal(self):
        geometry.coords_to_transform(np.identity(3))

    @pytest.mark.filterwarnings("ignore::RuntimeWarning")
    @pytest.mark.xfail(reason="edge-case where computed axes are"
                              "parallel") # (strict=True)
    def test_degenerate(self):
        singular = np.array([[1, 0, 0], [0, 0, 0], [2, 0, 0]])

        geometry.coords_to_transform(singular)

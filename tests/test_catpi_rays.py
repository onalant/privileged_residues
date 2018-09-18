import pytest

from numpy.testing import assert_allclose

from privileged_residues.chemical import catpi

def test_cat_pi(dummy_res, selector):
    rays = catpi.rays(dummy_res.pose, selector)

    assert_allclose(rays, dummy_res.cat_pi)

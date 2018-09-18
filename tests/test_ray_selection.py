import pytest

from .util import rays_allclose

from privileged_residues.chemical import bidentate

def test_n_rays(dummy_res, selector):
    selected = selector.apply(dummy_res.pose)

    rays = bidentate._n_rays(dummy_res.pose, selected)

    rays_allclose(rays, dummy_res.n_rays)

def test_c_rays(dummy_res, selector):
    selected = selector.apply(dummy_res.pose)

    rays = bidentate._c_rays(dummy_res.pose, selected)

    rays_allclose(rays, dummy_res.c_rays)

def test_sc_donor(dummy_res, selector):
    selected = selector.apply(dummy_res.pose)

    rays = bidentate._sc_donor(dummy_res.pose, selected)

    rays_allclose(rays, dummy_res.sc_donor)

def test_sc_acceptor(dummy_res, selector):
    selected = selector.apply(dummy_res.pose)

    rays = bidentate._sc_acceptor(dummy_res.pose, selected)

    rays_allclose(rays, dummy_res.sc_acceptor)


from numpy.testing import assert_allclose
from privileged_residues.geometry import create_ray

def pick_ray(res, center, base):
    return create_ray(res.xyz(center), res.xyz(base))

def rays_allclose(x, y):
    assert(len(x) == len(y))

    for k in y:
        assert_allclose(x[k], y[k])

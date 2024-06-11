
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 == 1 or max(xs) == 0:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")
    x = 0
    while poly(xs, x) != 0:
        x += 0.01
    return x


def test_poly():
    assert poly([1, 2], 0) == 1
    assert poly([1, 2], 1) == 3
    assert poly([1, 2

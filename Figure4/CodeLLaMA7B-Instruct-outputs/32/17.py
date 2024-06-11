
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if max(xs) == 0:
        raise ValueError("xs must have non-zero coefficients")
    x0 = -1
    while True:
        x1 = x0 - poly(xs, x0) / poly(xs, x0)
        if abs(x1 - x0) < 1e-10:
            return x1
        x0 = x1


if

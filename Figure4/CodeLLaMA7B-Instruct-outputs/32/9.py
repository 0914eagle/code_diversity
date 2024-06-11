
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if xs[-1] == 0:
        raise ValueError("xs must have non-zero coefficient")
    x0 = -xs[-1] / (xs[-2] + 1)
    while True:
        x1 = poly(xs, x0)
        if abs(x1) < 1e-6:
            return x0
        x0 = x1


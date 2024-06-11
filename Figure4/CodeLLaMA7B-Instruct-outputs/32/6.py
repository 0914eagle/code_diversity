
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if xs[n // 2] == 0:
        raise ValueError("largest coefficient must be non-zero")
    x0 = -xs[n // 2] / (2 * xs[n // 2 - 1])
    while True:
        x1 = x0 - poly(xs, x0) / poly(xs, x1)
        if abs(x1 - x0) < 1e-6:
            return x1
        x0 = x1


if

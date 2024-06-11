
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    n = len(xs) - 1
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if xs[n // 2] == 0:
        raise ValueError("largest non zero coefficient must be non zero")
    x0 = -xs[n // 2] / (n // 2)
    while True:
        x1 = x0 - poly(xs, x0) / poly(xs, x0)
        if abs(x1 - x0) < 1e-6:
            return x1
        x0 = x1


if

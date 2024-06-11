
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    n = len(xs)
    if n % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if xs[n // 2] == 0:
        raise ValueError("largest non zero coefficient must be non zero")
    left = -1
    right = 1
    while abs(right - left) > 1e-6:
        mid = (left + right) / 2
        if poly(xs, mid) < 0:
            left = mid
        else:
            right = mid
    return (left + right) / 2


if

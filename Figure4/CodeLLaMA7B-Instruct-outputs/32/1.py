
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 == 1 or not xs:
        raise ValueError("xs must have even number of coefficients")
    max_coeff = max(xs)
    if max_coeff == 0:
        raise ValueError("max coefficient must be non zero")
    x0 = -max_coeff
    while poly(xs, x0) != 0:
        x0 += max_coeff
    return x0


if __name__ == "__main__":
    print(round(poly([

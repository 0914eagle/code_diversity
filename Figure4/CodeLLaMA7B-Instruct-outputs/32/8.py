
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0 or max(xs) == 0:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")
    x0 = -1
    while poly(xs, x0) != 0:
        x0 += 0.1
    return x0


if __name__ == "__main__":
    print(round(poly([1, 2], 1), 2))  # f(x) = 1 + 2x
    print

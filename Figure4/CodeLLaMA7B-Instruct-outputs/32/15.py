
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    if max(xs) == 0:
        raise ValueError("xs must have non-zero coefficients")
    x0 = -1
    while poly(xs, x0) != 0:
        x0 += 0.1
    return x0


if __name__ == "__main__":
    print(find_zero([1, 2]))
    print(find_zero([-6, 11, -6, 1]))


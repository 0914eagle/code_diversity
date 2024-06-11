
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    if len(xs) % 2 != 0 or max(xs) == 0:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")
    x = 0
    while poly(xs, x) != 0:
        x += 0.01
    return x


if __name__ == "__main__":
    print(find_zero([1, 2]))
    print(find_zero([-6, 11, -6, 1]))
[/

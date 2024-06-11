
import math


def poly(xs: list, x: float):
    
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    
    n = len(xs) - 1
    if n % 2 != 0 or xs[0] == 0:
        raise ValueError("xs must have even number of coefficients and largest non zero coefficient")
    x0 = -xs[n] / xs[n - 1]
    while True:
        x1 = x0 - poly(xs, x0) / poly(xs, x0)
        if abs(x1 - x0) < 1e-6:
            return x1
        x0 = x1


if __name__ == "__main__":
    print(round(find

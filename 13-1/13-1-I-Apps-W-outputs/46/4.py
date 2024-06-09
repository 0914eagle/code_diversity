
import math

def solve(n, r, x):
    y = [10**100] * n
    for i in range(n):
        y[i] = y[i] - math.sqrt(r**2 - (x[i] - x[i-1])**2) if i > 0 else y[i] - r
    return y


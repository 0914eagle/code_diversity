
import math

def compute_e(n):
    return sum(1/math.factorial(i) for i in range(n+1))



import math

def e_approximation(n):
    return sum(1/math.factorial(i) for i in range(n+1))



import math

def solve(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (math.log(n) / (s / v)) ** (1 / (2 * math.sqrt(2)))
    t = (n * (math.log(n) ** (c * math.sqrt(2))) / (p * 1000000000))

    # Calculate the time it takes to distribute the keys
    t += s / v

    return t, c


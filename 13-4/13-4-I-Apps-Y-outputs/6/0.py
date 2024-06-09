
import math

def solve(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (math.log(n) / (s / v)) ** (1 / (2 * math.sqrt(2)))
    t_algorithm = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 1000000000)
    
    # Calculate the total time it takes to run the algorithm and distribute the keys
    t_total = t_algorithm + s / v
    
    return t_total, c


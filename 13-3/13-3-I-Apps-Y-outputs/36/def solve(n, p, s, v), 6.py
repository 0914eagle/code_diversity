
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    t_algorithm = s * (math.log(n) ** (1.5 * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    t_tour = s / v
    
    # Calculate the optimal value of c
    c = (t_tour / t_algorithm) - 1
    
    # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys
    t = t_algorithm + t_tour
    
    return t, c


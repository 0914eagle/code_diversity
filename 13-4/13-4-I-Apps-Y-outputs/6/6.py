
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    t_algo = s * (math.log(n) ** (1.5 * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    t_tour = s / v
    
    # Calculate the optimal value of c
    c = (t_algo / t_tour - 1) / (1 + 1 / c)
    
    # Return the time it takes for Miroslava to first run the algorithm and then distribute all the keys
    return t_algo, c

n = 10
p = 8.9
s = 40075000
v = 272.1
print(solve(n, p, s, v))


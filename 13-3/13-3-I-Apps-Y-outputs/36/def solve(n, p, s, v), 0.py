
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    t_algo = s * (math.log(n) ** (c * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    t_tour = s * (1 + 1/c) / v
    
    # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys
    t_total = t_algo + t_tour
    
    # Return the optimal value of c and the total time
    return c, t_total

# Test the function with the sample input
n = 10
p = 8.9
s = 40075000
v = 272.1
print(solve(n, p, s, v))


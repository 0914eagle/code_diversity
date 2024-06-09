
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    t_algorithm = s * (math.log2(n) ** (c * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    t_tour = s * (1 + 1/c) / v
    
    # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys
    t_total = t_algorithm + t_tour
    
    # Calculate the value of c that gives the optimal time
    c = (t_total * p * 1e9) / (s * math.log2(n) ** (c * math.sqrt(2)))
    
    return t_total, c

n = 10
p = 8.9
s = 40075000
v = 272.1

t_total, c = solve(n, p, s, v)
print(t_total, c)


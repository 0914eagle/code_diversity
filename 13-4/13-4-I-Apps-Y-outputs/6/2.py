
import math

def solve(n, p, s, v):
    # Calculate the time it takes for the algorithm to run
    time_algorithm = s * (math.log(n) ** (c * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes for Miroslava to complete the tour
    time_tour = s * (1 + 1 / c) / v
    
    # Calculate the total time it takes for Miroslava to run the algorithm and complete the tour
    time_total = time_algorithm + time_tour
    
    # Calculate the value of c that gives the optimal time
    c = (time_total / time_algorithm) - 1
    
    return time_total, c

n = 10
p = 8.9
s = 40075000
v = 272.1

time_total, c = solve(n, p, s, v)

print(time_total)
print(c)


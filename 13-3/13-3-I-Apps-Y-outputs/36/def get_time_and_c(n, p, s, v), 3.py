
import math

def get_time_and_c(n, p, s, v):
    # Calculate the time it takes for the algorithm to run with the optimal parameter c
    c = (math.log(n) / (s / v)) ** (1 / (2 * math.log(2)))
    time_algorithm = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 1000000000)
    
    # Calculate the total time it takes for Miroslava to run the algorithm and distribute the keys
    time_total = time_algorithm + s / v
    
    return time_total, c

n = 10
p = 8.9
s = 40075000
v = 272.1

time_total, c = get_time_and_c(n, p, s, v)

print(time_total)
print(c)


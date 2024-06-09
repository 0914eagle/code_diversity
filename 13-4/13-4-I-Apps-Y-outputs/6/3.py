
import math

def get_time_and_c(n, p, s, v):
    # Calculate the time it takes for the algorithm to run with the optimal parameter c
    c = (math.log(n) / (s / v)) ** (1 / (2 * math.sqrt(2)))
    time = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 1000000000)
    
    # Calculate the time it takes for Miroslava to distribute the keys
    distribute_time = s / v
    
    # Return the total time and the value of c
    return time + distribute_time, c

n, p, s, v = map(float, input().split())
time, c = get_time_and_c(n, p, s, v)
print(f"{time:.6f} {c:.6f}")


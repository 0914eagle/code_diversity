
import math

def get_time_and_c(n, p, s, v):
    # Calculate the optimal parameter c for the Arora-Mitchell algorithm
    c = (math.log(n) * math.sqrt(2)) / (v * 1000000000)
    
    # Calculate the time it takes to run the algorithm and distribute the keys
    time = s / (v * (1 + 1/c))
    
    return time, c

n = int(input())
p = float(input())
s = float(input())
v = float(input())

time, c = get_time_and_c(n, p, s, v)

print(time)
print(c)


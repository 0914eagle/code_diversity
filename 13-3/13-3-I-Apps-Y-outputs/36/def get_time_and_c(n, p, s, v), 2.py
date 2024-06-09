
import math

def get_time_and_c(n, p, s, v):
    # Calculate the time it takes to run the algorithm with the optimal parameter c
    c = (math.log(n) * math.sqrt(2)) / (p * 1e9)
    time_algorithm = n * (math.log(n) ** (c * math.sqrt(2))) / (p * 1e9)
    
    # Calculate the time it takes to complete the tour
    time_tour = s / v
    
    # Calculate the total time
    time = time_algorithm + time_tour
    
    return time, c

n = 10
p = 8.9
s = 40075000
v = 272.1

time, c = get_time_and_c(n, p, s, v)
print(time)
print(c)


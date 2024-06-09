
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)
    
    # Calculate the number of ways to place the obstacles in each subgrid
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            num_ways *= (i * j) % p
    
    return num_ways % p

n, m, p = map(int, input().split())
print(count_ways(n, m, p))


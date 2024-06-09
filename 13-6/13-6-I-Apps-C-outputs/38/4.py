
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)
    
    # Calculate the number of ways to place the obstacles in the grid
    num_ways *= math.factorial(n * m - num_obstacles)
    
    # Calculate the number of ways to place the obstacles in each subgrid
    for i in range(1, n // 2 + 1):
        for j in range(1, m // 2 + 1):
            num_ways *= math.factorial(i * j)
    
    # Return the number of ways modulo p
    return num_ways % p


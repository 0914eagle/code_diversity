
import math

def count_ways(n, m, p):
    # Calculate the number of obstacles needed to cover the grid
    num_obstacles = (n // 2) * (m // 2)
    
    # Calculate the number of ways to place the obstacles
    ways = math.factorial(num_obstacles)
    
    # Return the result modulo p
    return ways % p


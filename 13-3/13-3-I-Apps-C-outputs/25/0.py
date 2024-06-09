
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)

    # Calculate the number of ways to place the obstacles in the grid
    num_ways *= math.factorial(n * m - num_obstacles)

    # Calculate the number of ways to place the obstacles in the grid with at least one obstacle in each 2x2 subgrid
    num_ways //= math.factorial(n * m - (n // 2) * (m // 2))

    # Return the result modulo p
    return num_ways % p


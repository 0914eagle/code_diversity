
import math

def solve(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)

    # Calculate the number of ways to place the obstacles in the grid
    num_ways *= math.factorial(n * m - num_obstacles)

    # Calculate the number of ways to place the obstacles in the grid modulo p
    return num_ways % p


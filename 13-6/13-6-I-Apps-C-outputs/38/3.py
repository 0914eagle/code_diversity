
import math

def solve(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)

    # Calculate the number of ways to place the obstacles in each cell
    num_cells = n * m
    num_cell_ways = math.factorial(num_cells)

    # Calculate the final answer by dividing the number of ways to place the obstacles by the number of ways to place them in each cell
    answer = num_ways // num_cell_ways

    # Return the answer modulo p
    return answer % p


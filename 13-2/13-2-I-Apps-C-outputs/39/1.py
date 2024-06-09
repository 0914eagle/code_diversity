
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)

    # Calculate the number of ways to place the obstacles in each cell
    for i in range(n):
        for j in range(m):
            if i % 2 == 0 and j % 2 == 0:
                num_ways = (num_ways * 2) % p
            else:
                num_ways = (num_ways * 4) % p

    return num_ways


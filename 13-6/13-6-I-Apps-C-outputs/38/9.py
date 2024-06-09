
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_obstacles = (n // 2) * (m // 2)
    num_ways = math.factorial(num_obstacles)

    # Calculate the number of ways to place the obstacles in each row
    for i in range(n):
        num_ways //= math.factorial(math.floor(i / 2))

    # Calculate the number of ways to place the obstacles in each column
    for j in range(m):
        num_ways //= math.factorial(math.floor(j / 2))

    # Return the result modulo p
    return num_ways % p


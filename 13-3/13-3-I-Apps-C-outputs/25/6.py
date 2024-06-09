
import math

def count_ways(n, m, p):
    # Calculate the number of ways to place the minimum number of obstacles
    num_ways = 0
    for i in range(n - 1):
        for j in range(m - 1):
            # Check if the current subgrid contains at least one obstacle
            if not (i == 0 and j == 0) and not (i == n - 2 and j == m - 2):
                num_ways += 1
    
    # Return the number of ways modulo p
    return num_ways % p



import math

def solve(n, m, p):
    # Calculate the number of rows and columns that contain at least one obstacle
    num_rows = (n + 1) // 2
    num_cols = (m + 1) // 2
    
    # Calculate the number of ways to place the minimum number of obstacles
    num_ways = math.factorial(num_rows) * math.factorial(num_cols)
    
    # Return the result modulo p
    return num_ways % p


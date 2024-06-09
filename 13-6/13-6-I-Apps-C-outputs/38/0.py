
import math

def count_ways(n, m, p):
    # Calculate the number of rows and columns that need to have obstacles
    rows_needed = int(math.ceil(n / 2.0))
    cols_needed = int(math.ceil(m / 2.0))
    
    # Initialize the number of ways to place obstacles
    ways = 1
    
    # Loop through each row and column and calculate the number of ways to place obstacles
    for i in range(rows_needed):
        for j in range(cols_needed):
            ways = (ways * (n - i) * (m - j)) % p
    
    return ways


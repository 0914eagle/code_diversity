
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_buckets = capacity
    num_fills = 0

    # Loop through the wells and buckets
    for i in range(num_rows):
        for j in range(num_cols):
            # If the well has water and the bucket has capacity, fill the bucket
            if grid[i][j] == 1 and num_buckets > 0:
                num_buckets -= 1
                grid[i][j] = 0
                num_fills += 1
    
    # Return the number of fills
    return num_fills


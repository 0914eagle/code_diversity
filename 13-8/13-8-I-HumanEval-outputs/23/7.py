
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_wells = sum(row.count(1) for row in grid)
    num_buckets = capacity * num_cols
    num_lowers = 0

    # Loop through the wells and determine how many times to lower the buckets
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == 1:
                num_lowers += 1

    # Return the number of times to lower the buckets
    return num_lowers


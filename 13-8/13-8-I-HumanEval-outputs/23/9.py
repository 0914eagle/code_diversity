
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    

    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    num_lowerings = 0

    # Loop through each well and bucket
    for i in range(num_wells):
        for j in range(num_buckets):
            # Check if the bucket is full
            if grid[i][j] == 1:
                # Lower the bucket
                num_lowerings += 1
                # Empty the bucket
                grid[i][j] = 0
                # Break out of the loop
                break

    return num_lowerings


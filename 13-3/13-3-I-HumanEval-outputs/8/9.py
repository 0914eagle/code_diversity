
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_wells = num_rows * num_cols
    num_buckets = capacity
    num_lowerings = 0

    # Loop through each well and bucket
    for well_index in range(num_wells):
        # Calculate the row and column of the current well
        row = well_index // num_cols
        col = well_index % num_cols

        # Check if the well is empty
        if grid[row][col] == 0:
            continue

        # Check if the bucket is full
        if num_buckets == 0:
            num_lowerings += 1
            num_buckets = capacity

        # Lower the bucket into the well
        num_buckets -= 1
        grid[row][col] -= 1

    return num_lowerings



from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    num_lowerings = 0

    # Loop through each well and bucket
    for well in grid:
        for bucket in range(num_buckets):
            # Check if the bucket can be filled with water from the well
            if well[bucket] == 1:
                # Lower the bucket and increment the number of lowerings
                well[bucket] = 0
                num_lowerings += 1
                break

    # Return the number of lowerings
    return num_lowerings


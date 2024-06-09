
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    num_fills = 0

    # Loop through each well and bucket
    for well in grid:
        for bucket in range(num_buckets):
            # Check if the bucket can be filled with water from the well
            if well[bucket] == 1:
                # Increment the number of fills
                num_fills += 1
                # Set the well and bucket to empty
                well[bucket] = 0
                break

    return num_fills


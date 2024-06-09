
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    

    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    num_fills = 0

    # Loop through each well and bucket
    for well in grid:
        for i in range(num_buckets):
            # Check if the well is empty
            if well[i] == 0:
                break
            # Fill the bucket with water from the well
            num_fills += 1
    
    return num_fills


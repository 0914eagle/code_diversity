
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    num_fills = 0

    # Loop through the wells and buckets
    for well in grid:
        for bucket in range(num_buckets):
            # Check if the bucket is full
            if bucket == num_buckets - 1:
                # If the bucket is full, empty it and increment the number of fills
                num_fills += 1
                break
            # Check if the well has water
            if well[bucket] == 1:
                # If the well has water, empty the bucket and increment the number of fills
                num_fills += 1
                break
    
    return num_fills


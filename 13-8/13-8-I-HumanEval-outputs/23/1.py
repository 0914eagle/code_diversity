
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    num_columns = len(grid[0])
    num_buckets = capacity
    num_fills = 0

    # Iterate through the wells and buckets
    for well in range(num_wells):
        for bucket in range(num_buckets):
            # Check if the current bucket can fill the current well
            if grid[well][bucket] == 1:
                # Increment the number of fills and break the loop
                num_fills += 1
                break
    
    return num_fills


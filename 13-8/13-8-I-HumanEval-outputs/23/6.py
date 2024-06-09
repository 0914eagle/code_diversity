
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    well_length = len(grid[0])
    num_buckets = capacity
    num_lowerings = 0

    # Loop through the wells and buckets
    for i in range(num_wells):
        for j in range(well_length):
            if grid[i][j] == 1:
                num_buckets -= 1
                if num_buckets == 0:
                    num_lowerings += 1
                    num_buckets = capacity

    return num_lowerings


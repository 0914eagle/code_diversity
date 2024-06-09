
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    well_length = len(grid[0])
    num_buckets = capacity
    num_fills = 0

    # Iterate through the wells and calculate the number of fills required
    for i in range(num_wells):
        # Calculate the number of fills required for the current well
        num_fills += (grid[i].count(1) - 1) // num_buckets + 1

    return num_fills


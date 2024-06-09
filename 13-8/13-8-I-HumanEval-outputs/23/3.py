
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    # Initialize variables
    num_wells = len(grid)
    num_buckets = capacity
    total_water = sum(sum(row) for row in grid)
    num_bucket_fills = 0

    # Iterate through the wells
    for well in grid:
        # Check if the well can be emptied using the current number of bucket fills
        if sum(well) <= num_buckets:
            # Empty the well and update the number of bucket fills
            num_bucket_fills += 1
            num_buckets -= sum(well)
        else:
            # Calculate the number of bucket fills needed to empty the well
            num_bucket_fills += ceil(sum(well) / num_buckets)
            num_buckets = capacity - (sum(well) % num_buckets)

    return num_bucket_fills


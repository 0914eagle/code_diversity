
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid_values = []
    for row in grid:
        grid_values.extend(row)
    
    # Initialize the minimum path with the first value
    min_path = [grid_values[0]]
    
    # Iterate through the remaining values
    for i in range(1, len(grid_values)):
        # If the current value is not in the minimum path, add it
        if grid_values[i] not in min_path:
            min_path.append(grid_values[i])
        
        # If the length of the minimum path is equal to the given length, return it
        if len(min_path) == k:
            return min_path
    
    # If the minimum path is not found, return an empty list
    return []


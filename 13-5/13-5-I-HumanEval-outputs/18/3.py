
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[val for val in row] for row in grid]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the current row
        min_val = min(grid[i % len(grid)])
        
        # Add the minimum value to the minimum path
        min_path.append(min_val)
        
        # Update the grid by removing the minimum value
        for row in grid:
            row.remove(min_val)
    
    return min_path


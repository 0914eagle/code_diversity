
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first value
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the current row
        min_value = min(grid[0])
        
        # Find the column index of the minimum value
        min_index = grid[0].index(min_value)
        
        # Add the minimum value to the minimum path
        min_path.append(min_value)
        
        # Remove the minimum value from the current row
        grid[0].remove(min_value)
        
        # Move to the next row
        grid = [grid[i][1:] for i in range(1, len(grid))] + [grid[0]]
    
    return min_path


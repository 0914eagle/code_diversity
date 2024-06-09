
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first value
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the remaining cells
        min_value = min([grid[i][j] for j in range(len(grid[i])) if grid[i][j] not in min_path])
        
        # Add the minimum value to the minimum path
        min_path.append(min_value)
    
    return min_path


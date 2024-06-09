
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the neighbor cell with the minimum value
        min_value = float('inf')
        min_cell = None
        for j in range(len(grid[0])):
            for k in range(len(grid)):
                if grid[k][j] < min_value and [j, k] not in min_path:
                    min_value = grid[k][j]
                    min_cell = [j, k]
        
        # Add the minimum cell to the minimum path
        min_path.append(min_cell)
    
    # Return the minimum path
    return min_path


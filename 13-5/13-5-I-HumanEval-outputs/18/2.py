
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the cell with the minimum value that is a neighbor of the current cell
        min_value = float('inf')
        min_cell = None
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[j][k] < min_value and (j, k) not in min_path:
                    min_value = grid[j][k]
                    min_cell = (j, k)
        
        # Add the minimum cell to the minimum path
        min_path.append(min_value)
    
    return min_path

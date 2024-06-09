
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the current row
        min_value = min([grid[min_path[-1] // len(grid)][j] for j in range(len(grid[0]))])
        
        # Find the cell with the minimum value
        min_cell = [j for j in range(len(grid[0])) if grid[min_path[-1] // len(grid)][j] == min_value][0]
        
        # Add the minimum cell to the minimum path
        min_path.append(min_cell + min_path[-1] // len(grid) * len(grid))
    
    return min_path



from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the neighboring cell with the minimum value
        min_value = float('inf')
        for j in range(len(grid)):
            for l in range(len(grid[j])):
                if grid[j][l] < min_value and [j, l] not in min_path:
                    min_value = grid[j][l]
                    min_cell = [j, l]
        
        # Add the minimum cell to the minimum path
        min_path.append(min_value)
        grid[min_cell[0]][min_cell[1]] = float('inf')
    
    return min_path


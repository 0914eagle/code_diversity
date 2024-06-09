
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the current row
        min_value = min(grid[i % len(grid)])
        
        # Find the column index of the minimum value
        min_index = grid[i % len(grid)].index(min_value)
        
        # Add the minimum value to the minimum path
        min_path.append(min_value)
        
        # Update the grid by removing the minimum value and shifting the remaining values
        grid[i % len(grid)].pop(min_index)
        grid[(i + 1) % len(grid)].insert(0, min_value)
    
    return min_path


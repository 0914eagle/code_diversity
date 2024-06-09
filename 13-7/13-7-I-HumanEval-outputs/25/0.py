
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = grid
    k = k

    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]

    # Loop through the cells of the grid
    for i in range(1, k):
        # Find the neighbor cell with the minimum value
        min_value = float('inf')
        min_cell = None
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[j][k] < min_value and (j, k) not in min_path:
                    min_value = grid[j][k]
                    min_cell = (j, k)

        # Add the minimum cell to the minimum path
        min_path.append(min_cell)

    # Return the ordered list of the values on the cells that the minimum path go through
    return [grid[cell[0]][cell[1]] for cell in min_path]


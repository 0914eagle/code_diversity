
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the minimum path as the first cell
    min_path = [grid[0][0]]

    # Loop through the remaining cells
    for i in range(1, k):
        # Find the neighbor cell with the minimum value
        min_value = float('inf')
        for j in range(rows):
            for k in range(cols):
                if grid[j][k] < min_value and (j, k) not in min_path:
                    min_value = grid[j][k]
                    min_cell = (j, k)

        # Add the minimum cell to the path
        min_path.append(min_value)

    return min_path


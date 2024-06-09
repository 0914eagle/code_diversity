
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the minimum path as the first cell
    min_path = [grid[0][0]]

    # Loop through the remaining cells
    for i in range(1, k):
        # Find the neighbor cells that are not in the minimum path yet
        neighbor_cells = []
        for j in range(rows):
            for k in range(cols):
                if grid[j][k] not in min_path:
                    neighbor_cells.append((grid[j][k], abs(j - min_path[-1][0]), abs(k - min_path[-1][1])))
        
        # Sort the neighbor cells based on their distance from the last cell in the minimum path
        neighbor_cells.sort(key=lambda x: (x[1], x[2]))

        # Add the closest neighbor cell to the minimum path
        min_path.append(neighbor_cells[0][0])

    return min_path


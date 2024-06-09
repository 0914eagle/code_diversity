
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the minimum path
    min_path = []

    # Loop through the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is part of the minimum path
            if grid[i][j] in min_path:
                # Add the current cell to the minimum path
                min_path.append(grid[i][j])

                # If the minimum path is of the desired length, return it
                if len(min_path) == k:
                    return min_path

    # If the minimum path is not of the desired length, return an empty list
    return []


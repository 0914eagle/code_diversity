
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[0] + row + [0] for row in grid]
    grid.insert(0, [0] * len(grid[0]))
    grid.append([0] * len(grid[0]))

    # Initialize the minimum path with the first cell
    min_path = [grid[1][1]]

    # Loop through the cells of the grid
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            # If the current cell is not part of the minimum path, skip it
            if grid[i][j] == 0:
                continue

            # If the current cell is the last cell of the minimum path, add it to the path
            if len(min_path) == k:
                min_path.append(grid[i][j])
                break

            # If the current cell is not the last cell of the minimum path, check if it is a better option
            if grid[i][j] < min_path[-1]:
                min_path.append(grid[i][j])

    return min_path


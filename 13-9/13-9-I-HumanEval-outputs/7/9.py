
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the distances from the starting cell to all the cells
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    distances[0][0] = 0

    # Initialize the previous cell for each cell
    previous = [[(0, 0) for _ in range(cols)] for _ in range(rows)]
    previous[0][0] = (0, 0)

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is not the starting cell, check if the distance from the starting cell to the current cell is less than the minimum distance
            if (i, j) != (0, 0) and distances[i][j] > distances[i-1][j-1] + 1:
                # If the distance is less than the minimum distance, update the minimum distance and the previous cell
                distances[i][j] = distances[i-1][j-1] + 1
                previous[i][j] = (i-1, j-1)

    # Initialize the minimum path
    path = []

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is the starting cell, add the value to the minimum path
            if (i, j) == (0, 0):
                path.append(grid[i][j])

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is not the starting cell, check if the distance from the starting cell to the current cell is equal to the minimum distance
            if (i, j) != (0, 0) and distances[i][j] == distances[0][0]:
                # If the distance is equal to the minimum distance, add the value to the minimum path
                path.append(grid[i][j])

    # Return the minimum path
    return path


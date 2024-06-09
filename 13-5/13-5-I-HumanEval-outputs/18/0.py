
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the minimum path as the first row of the grid
    min_path = grid[0]

    # Loop through each row of the grid
    for i in range(1, len(grid)):
        # Loop through each element of the current row
        for j in range(len(grid[i])):
            # Check if the element is in the minimum path
            if grid[i][j] in min_path:
                # If it is, replace it with the next element in the row
                min_path[min_path.index(grid[i][j])] = grid[i][(j+1)%len(grid[i])]

    # Return the minimum path
    return min_path


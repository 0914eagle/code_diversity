
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the minimum path as the first row of the grid
    min_path = grid[0]
    # Loop through the remaining rows of the grid
    for i in range(1, len(grid)):
        # Loop through the elements of the current row
        for j in range(len(grid[i])):
            # If the current element is less than the minimum element of the minimum path,
            # replace the minimum element of the minimum path with the current element
            if grid[i][j] < min_path[0]:
                min_path[0] = grid[i][j]
            # If the current element is greater than the minimum element of the minimum path,
            # but less than the second element of the minimum path, replace the second element
            # of the minimum path with the current element
            elif grid[i][j] < min_path[1]:
                min_path[1] = grid[i][j]
    return min_path


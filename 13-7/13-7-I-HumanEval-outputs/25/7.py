
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the minimum path to be the first row of the grid
    min_path = grid[0]

    # Iterate over the remaining rows of the grid
    for i in range(1, len(grid)):
        # Initialize the current path to be the first element of the current row
        current_path = [grid[i][0]]

        # Iterate over the remaining elements of the current row
        for j in range(1, len(grid[i])):
            # If the current element is less than the last element of the current path,
            # update the current path to include the current element
            if grid[i][j] < current_path[-1]:
                current_path.append(grid[i][j])
            # If the current element is greater than or equal to the last element of the current path,
            # update the minimum path if the current path is shorter than the minimum path
            elif len(current_path) < len(min_path):
                min_path = current_path

    # Return the minimum path
    return min_path


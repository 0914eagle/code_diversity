
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid_values = grid

    # Initialize the minimum path with the first value
    min_path = [grid_values[0][0]]

    # Loop through the remaining cells
    for i in range(1, k):
        # Find the minimum value in the current row
        min_value = min(grid_values[0])

        # Find the column index of the minimum value
        min_index = grid_values[0].index(min_value)

        # Add the minimum value to the minimum path
        min_path.append(min_value)

        # Remove the minimum value from the current row
        grid_values[0].remove(min_value)

        # Move to the next row
        grid_values = grid_values[1:]

        # Add the minimum value to the beginning of the next row
        grid_values[0].insert(min_index, min_value)

    return min_path


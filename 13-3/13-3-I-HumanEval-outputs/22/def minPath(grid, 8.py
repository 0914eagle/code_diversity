
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = grid
    # Initialize the minimum path as an empty list
    min_path = []
    # Initialize the current position as the top-left cell
    current_position = (0, 0)
    # Initialize the number of steps taken as 0
    num_steps = 0

    # While the number of steps taken is less than the given length k
    while num_steps < k:
        # Get the current cell value
        current_value = grid[current_position[0]][current_position[1]]
        # Add the current value to the minimum path
        min_path.append(current_value)
        # Increment the number of steps taken
        num_steps += 1
        # Get the neighbor cells of the current cell
        neighbor_cells = get_neighbor_cells(grid, current_position)
        # If there are no neighbor cells, return the minimum path
        if not neighbor_cells:
            return min_path
        # Get the neighbor cell with the minimum value
        min_neighbor_cell = min(neighbor_cells, key=lambda x: grid[x[0]][x[1]])
        # Set the current position to the minimum neighbor cell
        current_position = min_neighbor_cell

    # Return the minimum path
    return min_path

def get_neighbor_cells(grid, position):
    
    # Get the row and column indices of the given position
    row, col = position
    # Get the number of rows and columns in the grid
    num_rows, num_cols = len(grid), len(grid[0])
    # Initialize the neighbor cells as an empty list
    neighbor_cells = []

    # If the row index is not zero, add the cell above the current cell to the neighbor cells
    if row > 0:
        neighbor_cells.append((row - 1, col))
    # If the row index is not the last row, add the cell below the current cell to the neighbor cells
    if row < num_rows - 1:
        neighbor_cells.append((row + 1, col))
    # If the column index is not zero, add the cell to the left of the current cell to the neighbor cells
    if col > 0:
        neighbor_cells.append((row, col - 1))
    # If the column index is not the last column, add the cell to the right of the current cell to the neighbor cells
    if col < num_cols - 1:
        neighbor_cells.append((row, col + 1))

    # Return the neighbor cells
    return neighbor_cells


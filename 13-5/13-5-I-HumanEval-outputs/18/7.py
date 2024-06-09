
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = grid
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    # Initialize the current cell as the first cell
    current_cell = (0, 0)
    # Initialize the number of cells visited as 1
    num_cells_visited = 1

    # Loop until the minimum path has the required length
    while len(min_path) < k:
        # Get the neighbors of the current cell
        neighbors = get_neighbors(grid, current_cell)
        # Filter the neighbors that have not been visited yet
        unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in min_path]
        # If there are no unvisited neighbors, return an empty list
        if not unvisited_neighbors:
            return []
        # Select the neighbor with the smallest value
        next_cell = min(unvisited_neighbors, key=lambda x: grid[x[0]][x[1]])
        # Add the selected neighbor to the minimum path
        min_path.append(grid[next_cell[0]][next_cell[1]])
        # Update the current cell and the number of cells visited
        current_cell = next_cell
        num_cells_visited += 1

    # Return the minimum path
    return min_path

def get_neighbors(grid, cell):
    
    # Get the row and column indices of the cell
    row, col = cell
    # Get the number of rows and columns in the grid
    num_rows, num_cols = len(grid), len(grid[0])
    # Initialize the neighbors list
    neighbors = []

    # Add the neighboring cells to the list
    if row > 0:
        neighbors.append((row - 1, col))
    if row < num_rows - 1:
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col < num_cols - 1:
        neighbors.append((row, col + 1))

    # Return the neighbors list
    return neighbors


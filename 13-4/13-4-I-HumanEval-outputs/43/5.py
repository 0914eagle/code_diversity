
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Initialize the current cell as the first cell
    current_cell = (0, 0)
    
    # Loop until the minimum path has the required length
    while len(min_path) < k:
        # Get the neighbors of the current cell
        neighbors = get_neighbors(grid, current_cell)
        
        # Find the neighbor with the minimum value that is not in the minimum path
        min_value = float('inf')
        min_cell = None
        for neighbor in neighbors:
            if neighbor not in min_path and grid[neighbor[0]][neighbor[1]] < min_value:
                min_value = grid[neighbor[0]][neighbor[1]]
                min_cell = neighbor
        
        # If no neighbor has a value less than the minimum path, return an empty list
        if min_cell is None:
            return []
        
        # Add the minimum value to the minimum path and set the current cell to the minimum cell
        min_path.append(min_value)
        current_cell = min_cell
    
    # Return the minimum path
    return min_path

def get_neighbors(grid, cell):
    
    i, j = cell
    neighbors = []
    if i > 0:
        neighbors.append((i-1, j))
    if i < len(grid) - 1:
        neighbors.append((i+1, j))
    if j > 0:
        neighbors.append((i, j-1))
    if j < len(grid[0]) - 1:
        neighbors.append((i, j+1))
    return neighbors


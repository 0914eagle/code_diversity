
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the minimum path
    min_path = []

    # Initialize the visited cells
    visited = set()

    # Initialize the current cell
    current_cell = (0, 0)

    # Loop until we find the minimum path
    while len(min_path) < k:
        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, rows, cols)

        # Find the neighbor with the minimum value
        min_value = float('inf')
        min_neighbor = None
        for neighbor in neighbors:
            if grid[neighbor[0]][neighbor[1]] < min_value and neighbor not in visited:
                min_value = grid[neighbor[0]][neighbor[1]]
                min_neighbor = neighbor

        # Add the minimum neighbor to the path
        min_path.append(min_value)
        visited.add(min_neighbor)

        # Update the current cell
        current_cell = min_neighbor

    return min_path

def get_neighbors(cell, rows, cols):
    
    neighbors = []

    # Top neighbor
    if cell[0] > 0:
        neighbors.append((cell[0] - 1, cell[1]))

    # Bottom neighbor
    if cell[0] < rows - 1:
        neighbors.append((cell[0] + 1, cell[1]))

    # Left neighbor
    if cell[1] > 0:
        neighbors.append((cell[0], cell[1] - 1))

    # Right neighbor
    if cell[1] < cols - 1:
        neighbors.append((cell[0], cell[1] + 1))

    return neighbors


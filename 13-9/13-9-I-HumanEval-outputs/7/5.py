
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid_values = grid

    # Initialize the visited matrix with False
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the result list
    result = []

    # Start from the first cell
    current_cell = (0, 0)

    # While we still have cells to visit
    while k > 0:
        # If the current cell has not been visited
        if not visited[current_cell[0]][current_cell[1]]:
            # Mark the current cell as visited
            visited[current_cell[0]][current_cell[1]] = True

            # Add the value of the current cell to the result list
            result.append(grid_values[current_cell[0]][current_cell[1]])

            # Decrement the number of cells to visit
            k -= 1

        # Find the next cell to visit
        neighbors = [(current_cell[0] - 1, current_cell[1]), (current_cell[0] + 1, current_cell[1]), (current_cell[0], current_cell[1] - 1), (current_cell[0], current_cell[1] + 1)]
        neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and not visited[neighbor[0]][neighbor[1]]]
        if len(neighbors) == 0:
            break
        current_cell = neighbors[0]

    # Return the result list
    return result


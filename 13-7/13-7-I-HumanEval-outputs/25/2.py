
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid_values = grid

    # Initialize the visited matrix with False
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the minimum path with the first value
    min_path = [grid_values[0][0]]

    # Initialize the current position as (0, 0)
    current_position = (0, 0)

    # While the minimum path is not of length k
    while len(min_path) < k:
        # Get the neighbors of the current position
        neighbors = get_neighbors(grid_values, current_position)

        # If there are no neighbors, return an empty list
        if not neighbors:
            return []

        # Find the neighbor with the minimum value that has not been visited
        min_value = float('inf')
        min_neighbor = None
        for neighbor in neighbors:
            if grid_values[neighbor[0]][neighbor[1]] < min_value and not visited[neighbor[0]][neighbor[1]]:
                min_value = grid_values[neighbor[0]][neighbor[1]]
                min_neighbor = neighbor

        # If there is no unvisited neighbor, return an empty list
        if min_neighbor is None:
            return []

        # Add the minimum neighbor to the minimum path
        min_path.append(min_value)

        # Mark the minimum neighbor as visited
        visited[min_neighbor[0]][min_neighbor[1]] = True

        # Set the current position to the minimum neighbor
        current_position = min_neighbor

    # Return the minimum path
    return min_path

def get_neighbors(grid: List[List[int]], position: tuple) -> List[tuple]:
    
    row, col = position
    neighbors = []

    # Up
    if row > 0:
        neighbors.append((row - 1, col))

    # Down
    if row < len(grid) - 1:
        neighbors.append((row + 1, col))

    # Left
    if col > 0:
        neighbors.append((row, col - 1))

    # Right
    if col < len(grid[0]) - 1:
        neighbors.append((row, col + 1))

    return neighbors



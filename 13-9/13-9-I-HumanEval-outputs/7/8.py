
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize a list to store the path
    path = []

    # Initialize the current position as (0, 0)
    current_position = (0, 0)

    # Loop until we have visited k cells
    while len(path) < k:
        # Get the neighbors of the current position
        neighbors = get_neighbors(grid, current_position)

        # If there are no neighbors, return an empty list
        if not neighbors:
            return []

        # Find the neighbor with the minimum value
        minimum_value = min(neighbors, key=neighbors.get)

        # Add the minimum value to the path
        path.append(minimum_value)

        # Update the current position to the neighbor with the minimum value
        current_position = minimum_value

    # Return the path
    return path

def get_neighbors(grid, position):
    
    neighbors = {}

    # Get the row and column of the current position
    row, col = position

    # Loop over the rows and columns of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # If the position is a neighbor of the current position
            if (r, c) in get_neighbor_positions(grid, position):
                # Add the position and value to the dictionary of neighbors
                neighbors[(r, c)] = grid[r][c]

    return neighbors

def get_neighbor_positions(grid, position):
    
    # Get the row and column of the current position
    row, col = position

    # Initialize a list to store the neighbor positions
    neighbor_positions = []

    # Loop over the rows and columns of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # If the position is a neighbor of the current position
            if (r, c) != position and (r, c) in get_adjacent_positions(grid, position):
                # Add the position to the list of neighbor positions
                neighbor_positions.append((r, c))

    return neighbor_positions

def get_adjacent_positions(grid, position):
    
    # Get the row and column of the current position
    row, col = position

    # Initialize a list to store the adjacent positions
    adjacent_positions = []

    # Loop over the rows and columns of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # If the position is adjacent to the current position
            if (r, c) != position and (abs(r - row) + abs(c - col)) == 1:
                # Add the position to the list of adjacent positions
                adjacent_positions.append((r, c))

    return adjacent_positions


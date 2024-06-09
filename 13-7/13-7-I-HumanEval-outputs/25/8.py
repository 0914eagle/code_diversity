
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    n = len(grid)
    values = [grid[i][j] for i in range(n) for j in range(n)]

    # Initialize the visited cells to False
    visited = [[False for _ in range(n)] for _ in range(n)]

    # Initialize the minimum path to empty
    min_path = []

    # Initialize the current cell to (0, 0)
    current_cell = (0, 0)

    # Loop until the minimum path has length k
    while len(min_path) < k:
        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, n)

        # Filter the neighbors that have not been visited
        unvisited_neighbors = [neighbor for neighbor in neighbors if not visited[neighbor[0]][neighbor[1]]]

        # If there are no unvisited neighbors, then the minimum path is not possible
        if not unvisited_neighbors:
            return []

        # Choose the neighbor with the minimum value
        min_value = min(values[neighbor[0] * n + neighbor[1]] for neighbor in unvisited_neighbors)
        min_neighbor = [neighbor for neighbor in unvisited_neighbors if values[neighbor[0] * n + neighbor[1]] == min_value][0]

        # Add the minimum neighbor to the minimum path
        min_path.append(values[min_neighbor[0] * n + min_neighbor[1]])

        # Mark the minimum neighbor as visited
        visited[min_neighbor[0]][min_neighbor[1]] = True

        # Set the current cell to the minimum neighbor
        current_cell = min_neighbor

    # Return the minimum path
    return min_path

def get_neighbors(cell: tuple, n: int) -> List[tuple]:
    
    i, j = cell
    neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n]



from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize a list to store the minimum path
    min_path = []
    # Initialize a set to store the visited cells
    visited = set()
    # Initialize a queue to store the cells to be visited
    queue = []
    # Add the first cell to the queue
    queue.append((0, 0))
    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        row, col = queue.pop(0)
        # If the current cell is not in the visited set, add it to the visited set and the minimum path
        if (row, col) not in visited:
            visited.add((row, col))
            min_path.append(grid[row][col])
            # If the length of the minimum path is equal to k, return it
            if len(min_path) == k:
                return min_path
            # Get the neighbors of the current cell
            neighbors = get_neighbors(grid, row, col)
            # Add the neighbors to the queue
            queue.extend(neighbors)
    
    # If the minimum path is not found, return an empty list
    return []

def get_neighbors(grid, row, col):
    
    # Initialize a list to store the neighbors
    neighbors = []
    # Check if the cell is not at the edge of the grid
    if row > 0 and col > 0 and row < len(grid) - 1 and col < len(grid[0]) - 1:
        # Add the top, bottom, left, and right neighbors to the list
        neighbors.append((row - 1, col))
        neighbors.append((row + 1, col))
        neighbors.append((row, col - 1))
        neighbors.append((row, col + 1))
    # Return the list of neighbors
    return neighbors




from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize a set to store the visited cells
    visited = set()
    # Initialize a queue to store the cells to visit
    queue = [(0, 0, 0)]
    # Initialize the minimum path length to infinity
    min_path_length = float('inf')
    # Initialize the minimum path
    min_path = []

    while queue:
        # Get the current cell and its distance from the starting cell
        cell, distance = queue.pop(0)
        # If the cell has already been visited, skip it
        if cell in visited:
            continue
        # If the cell is the goal cell, update the minimum path length and path
        if distance == k:
            min_path_length = distance
            min_path = [cell]
            break
        # Add the cell to the visited set
        visited.add(cell)
        # Get the neighbor cells of the current cell
        neighbors = get_neighbors(grid, cell)
        # Add the neighbor cells to the queue
        for neighbor in neighbors:
            queue.append((neighbor, distance+1))
    
    return min_path

def get_neighbors(grid, cell):
    
    row, col = cell
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < len(grid) - 1:
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col < len(grid[0]) - 1:
        neighbors.append((row, col+1))
    return neighbors


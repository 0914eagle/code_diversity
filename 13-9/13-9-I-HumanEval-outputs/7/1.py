
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid with the given values
    grid = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
    
    # Initialize the minimum path with the first cell
    min_path = [grid[0][0]]
    
    # Initialize the current cell as the first cell
    current_cell = (0, 0)
    
    # Loop until the length of the minimum path is k
    while len(min_path) < k:
        # Get the neighbors of the current cell
        neighbors = get_neighbors(grid, current_cell)
        
        # If there are no neighbors, return an empty list
        if not neighbors:
            return []
        
        # Find the neighbor with the smallest value that is not in the minimum path
        smallest_neighbor = min([n for n in neighbors if n not in min_path], key=lambda x: x[2])
        
        # Add the smallest neighbor to the minimum path
        min_path.append(smallest_neighbor[2])
        
        # Set the current cell to the smallest neighbor
        current_cell = smallest_neighbor[:2]
    
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
    if j < len(grid[i]) - 1:
        neighbors.append((i, j+1))
    return neighbors


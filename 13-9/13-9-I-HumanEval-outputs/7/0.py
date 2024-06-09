
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    
    # Initialize the grid
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    queue = [(0, 0, 1)]

    # Initialize the minimum path
    min_path = []

    while queue:
        # Get the current cell and the current length of the path
        row, col, length = queue.pop(0)

        # If the length of the path is equal to k, add the current cell to the minimum path
        if length == k:
            min_path.append(grid[row][col])
            continue

        # If the current cell has already been visited, skip it
        if visited[row][col]:
            continue

        # Mark the current cell as visited
        visited[row][col] = True

        # Add the neighbor cells to the queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < n and 0 <= c < n:
                queue.append((r, c, length+1))

    # Return the minimum path
    return min_path


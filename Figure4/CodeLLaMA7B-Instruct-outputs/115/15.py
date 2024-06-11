

def max_fill(grid, capacity):
    import math
    
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    bucket_count = 0
    total_water = 0

    # BFS to find the shortest path to fill the grid
    queue = [(0, 0, 0)]
    while queue:
        row, col, level = queue.pop(0)
        if visited[row][col]:
            continue
        visited[row][col] = True

        # If we reach the end of the grid, return the level
        if row == rows - 1:
            return level

        # Add neighbors to the queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                queue.append((r, c, level + 1))

    # Return -1 if we couldn't find a path to fill the grid
    return -1


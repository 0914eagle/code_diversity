

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    bucket_count = 0
    total_water = 0
    max_water = 0

    # BFS to find the maximum water that can be extracted
    queue = [(0, 0, 0)]
    while queue:
        row, col, water = queue.pop(0)
        if visited[row][col]:
            continue
        visited[row][col] = True
        total_water += water
        max_water = max(max_water, total_water)

        # Add neighbors to queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                queue.append((r, c, water + grid[r][c]))

    # Return the number of times we need to lower the buckets
    return math.ceil(max_water / capacity)


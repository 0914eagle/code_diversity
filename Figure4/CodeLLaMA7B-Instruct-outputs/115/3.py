

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_level = [0] * m
    total_level = 0
    moves = 0

    # BFS to find the maximum level of water in the grid
    queue = [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if not visited[i][j]:
            visited[i][j] = True
            total_level += grid[i][j]
            if i > 0 and not visited[i-1][j] and grid[i-1][j] > 0:
                queue.append((i-1, j))
            if j > 0 and not visited[i][j-1] and grid[i][j-1] > 0:
                queue.append((i, j-1))
            if i < m-1 and not visited[i+1][j] and grid[i+1][j] > 0:
                queue.append((i+1, j))
            if j < n-1 and not visited[i][j+1] and grid[i][j+1] > 0:
                queue.append((i, j+1))

    # DFS to find the maximum number of times we can empty the buckets
    for i in range(m):
        if grid[i][0] > 0:
            bucket_level[i] = grid[i][0]
            dfs(i, 0, visited, grid, bucket_level, capacity)

    # Return the maximum number of times we can empty the buckets
    return moves

def

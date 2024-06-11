

def max_fill(grid, capacity):
    import math
    
    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_count = 0
    total_water = 0

    # BFS to find the maximum water that can be filled
    queue = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True
                total_water += 1

    while queue:
        i, j = queue.pop(0)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = True
                total_water += 1

    # DFS to find the minimum number of buckets needed to empty the water
    bucket_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bucket_count += 1
                dfs(i, j, visited, grid, capacity)

    return bucket_count

def dfs(i, j, visited, grid, capacity):
    
    m, n = len(grid), len(grid[0])
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or visited[i][j]:
        return
    visited[i][j] = True
    if grid[i][j] > capacity:
        grid[i][j] = capacity
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj =

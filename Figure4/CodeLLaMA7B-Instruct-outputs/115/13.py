

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_count = 0
    total_water = 0
    max_fill = 0

    # BFS to find the maximum amount of water that can be filled
    queue = [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True
        total_water += grid[i][j]
        if total_water > max_fill:
            max_fill = total_water
        if i > 0 and not visited[i-1][j] and grid[i-1][j] > 0:
            queue.append((i-1, j))
        if j > 0 and not visited[i][j-1] and grid[i][j-1] > 0:
            queue.append((i, j-1))
        if i < m-1 and not visited[i+1][j] and grid[i+1][j] > 0:
            queue.append((i+1, j))
        if j < n-1 and not visited[i][j+1] and grid[i][j+1] > 0:
            queue.append((i, j+1))

    # DFS to find the minimum number of times the buckets need to be lowered
    queue = [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if grid[i][j] > 0:
            bucket_count += 1
        if i > 0 and not visited[i-1][j] and grid[i-1][j] > 0:
            queue.append((i-1, j))
        if j > 0 and not visited[i][j-1] and grid[i][j-1] > 0:
            queue.append((i, j-1))
        if i

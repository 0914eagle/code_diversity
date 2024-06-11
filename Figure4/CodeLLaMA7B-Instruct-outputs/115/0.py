

def max_fill(grid, capacity):
    import math
    
    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_count = 0
    total_water = 0

    # BFS to find the maximum amount of water that can be filled
    queue = [(0, 0, 0)]
    while queue:
        i, j, water = queue.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True
        total_water += water
        if grid[i][j] == 1:
            bucket_count += 1
        if i > 0 and not visited[i-1][j] and grid[i-1][j] == 1:
            queue.append((i-1, j, water+1))
        if j > 0 and not visited[i][j-1] and grid[i][j-1] == 1:
            queue.append((i, j-1, water+1))
        if i < m-1 and not visited[i+1][j] and grid[i+1][j] == 1:
            queue.append((i+1, j, water+1))
        if j < n-1 and not visited[i][j+1] and grid[i][j+1] == 1:
            queue.append((i, j+1, water+1))

    # Return the maximum amount of water that can be filled
    return total_water


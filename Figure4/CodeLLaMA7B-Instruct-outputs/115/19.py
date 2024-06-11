

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
                queue.append((i, j, 1))
                visited[i][j] = True
                total_water += 1
                bucket_count += 1

    while queue:
        i, j, water = queue.pop(0)

        # Check if the current well is full
        if water == capacity:
            continue

        # Check if the current well is the last well in the row
        if j == n - 1:
            next_j = 0
        else:
            next_j = j + 1

        # Check if the current well is the last well in the column
        if i == m - 1:
            next_i = 0
        else:
            next_i = i + 1

        # Check if the current well is not the last well in the row or column
        if next_j < n and not visited[i][next_j] and grid[i][next_j] == 1:
            queue.append((i, next_j, water + 1))
            visited[i][next_j] = True
            total_water += 1
            bucket_count += 1

        if next_i < m and not visited[next_i][j] and grid[next_i][j] == 1:
            queue.append((next_i, j, water + 1))
            visited[next_i][j] = True
            total_water += 1
            bucket_count += 1

    # Return the number of times you need to lower the buckets
    return bucket_count - total_water



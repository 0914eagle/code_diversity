

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    bucket_count = 0
    total_water = 0

    # BFS to find the shortest path to fill the grid
    queue = [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if visited[i][j]:
            continue
        visited[i][j] = True

        # If the current cell is a water cell, add it to the total water
        if grid[i][j] == 1:
            total_water += 1

        # If the current cell is at the edge of the grid or if the bucket capacity is full,
        # we need to lower the bucket
        if i == 0 or j == 0 or i == m - 1 or j == n - 1 or total_water == capacity:
            bucket_count += 1
            total_water = 0

        # Add the neighbors of the current cell to the queue
        for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                queue.append((ni, nj))

    # Return the number of times we need to lower the bucket
    return bucket_count

# Test case 1:
grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
print(max_fill(grid, capacity)) # Output: 6

# Test case 2:
grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
capacity = 2
print(max_fill(grid, capacity)) # Output: 5

# Test case 3:
grid = [[0,0,0], [0,0,0]]
capacity = 5
print

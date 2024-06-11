

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
        total_water += grid[i][j]
        if total_water == capacity:
            bucket_count += 1
            total_water = 0
        if i > 0 and not visited[i-1][j] and grid[i-1][j] == 1:
            queue.append((i-1, j))
        if j > 0 and not visited[i][j-1] and grid[i][j-1] == 1:
            queue.append((i, j-1))
        if i < m-1 and not visited[i+1][j] and grid[i+1][j] == 1:
            queue.append((i+1, j))
        if j < n-1 and not visited[i][j+1] and grid[i][j+1] == 1:
            queue.append((i, j+1))

    # Return the number of times you need to lower the buckets
    return bucket_count

# Test case 1:
grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
capacity = 1
print(max_fill(grid, capacity)) # Output: 6

def max_fill(grid, capacity):
    import math
    
    m, n = len(grid), len(grid[0])
    buckets = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                buckets[i][j] = capacity
            else:
                buckets[i][j] = 0
    for i in range(m):
        for j in range(n):
            if buckets[i][j] == capacity:
                buckets[i][j] = 0
            else:
                buckets[i][j] = capacity - buckets[i][j]
    return sum(buckets[i][j] for i in range(m) for j in range(n))



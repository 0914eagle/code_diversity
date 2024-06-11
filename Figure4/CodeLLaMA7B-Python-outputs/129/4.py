def minPath(grid, k):
    
    # Initialization
    n = len(grid)
    m = len(grid[0])
    if n < 2 or m < 2:
        return []
    if k > n * m:
        return []
    if k == 1:
        return [min(grid[0][0], grid[n - 1][m - 1])]

    # DFS
    
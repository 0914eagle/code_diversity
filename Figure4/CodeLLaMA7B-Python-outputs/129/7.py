def minPath(grid, k):
    
    n = len(grid)
    m = len(grid[0])
    if k > n*m:
        return []
    if k == 0:
        return []
    if k == 1:
        return [min(grid[0])]
    if k == 2:
        return [min(grid[0]), min(grid[1])]
    if k == n*m:
        return [grid[i][j] for i in range(n) for j in range(m)]

    # find the kth smallest value in the grid
    
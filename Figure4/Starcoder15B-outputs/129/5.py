def minPath(grid, k):
    
    N = len(grid)
    if N == 1:
        return [grid[0][0]]
    if k == 1:
        return [min(grid[0])]

    
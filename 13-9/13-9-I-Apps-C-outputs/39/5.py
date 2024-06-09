
def solve(n, a):
    # Check if the number of targets is valid
    if sum(a) > 2 * n:
        return -1
    
    # Initialize the grid with the targets
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(a[i]):
            grid[i + 1][j + 1] = 1
    
    # Check if the grid is valid
    for i in range(1, n + 1):
        if sum(grid[i]) > 2:
            return -1
    
    # Return the grid
    return grid



def solve(vault):
    # Initialize variables
    m, n = len(vault), len(vault[0])
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            grid[i + 1][j + 1] = max(grid[i][j + 1], grid[i + 1][j]) + vault[i][j]
    return grid[m][n]



def is_symmetric(grid):
    # Check if the grid is square
    if len(grid) != len(grid[0]):
        return False

    # Check if the grid is symmetric
    for i in range(len(grid)):
        for j in range(i):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False

    # If the grid is symmetric, return True
    return True


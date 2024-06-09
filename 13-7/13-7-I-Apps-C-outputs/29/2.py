
def is_symmetric(grid):
    # Check if the grid is a square
    if len(grid) != len(grid[0]):
        return "NO"

    # Check if the grid is symmetric
    for i in range(len(grid)):
        for j in range(i, len(grid[0])):
            if grid[i][j] != grid[len(grid) - 1 - i][len(grid[0]) - 1 - j]:
                return "NO"

    # If the grid is symmetric, return "YES"
    return "YES"



def solve(grid):
    # Initialize variables
    rows = len(grid)
    cols = len(grid[0])
    north_magnets = 0
    south_magnets = 0
    black_cells = 0

    # Count the number of south magnets and black cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "s":
                south_magnets += 1
            if grid[i][j] == "#":
                black_cells += 1

    # Check if it is possible to place magnets such that the conditions are met
    if south_magnets < rows and south_magnets < cols:
        return -1

    # Count the number of north magnets required
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "b":
                north_magnets += 1

    return north_magnets


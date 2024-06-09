
def solve(grid):
    # Initialize the variables
    rows, cols = len(grid), len(grid[0])
    north_magnets, south_magnets = 0, 0
    black_cells, white_cells = set(), set()

    # Loop through the grid and count the number of north and south magnets
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "N":
                north_magnets += 1
            elif grid[i][j] == "S":
                south_magnets += 1

    # Loop through the grid and find the black and white cells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                black_cells.add((i, j))
            elif grid[i][j] == ".":
                white_cells.add((i, j))

    # Check if it is possible to place magnets such that the conditions are met
    if len(black_cells) > 0 and len(white_cells) > 0 and north_magnets >= south_magnets:
        return north_magnets
    else:
        return -1



def solve(grid):
    # Initialize variables
    n, m = len(grid), len(grid[0])
    north_magnets, south_magnets = 0, 0
    row_south_magnets, col_south_magnets = [0] * n, [0] * m
    black_cells = []

    # Count the number of south magnets and black cells
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                black_cells.append((i, j))
            elif grid[i][j] == "#":
                south_magnets += 1
                row_south_magnets[i] += 1
                col_south_magnets[j] += 1

    # Check if it is possible to place magnets such that the conditions are met
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                # If there is no south magnet in this row or column, return -1
                if row_south_magnets[i] == 0 or col_south_magnets[j] == 0:
                    return -1
            elif grid[i][j] == "#":
                # If there is no north magnet in this cell, return -1
                if north_magnets == 0:
                    return -1
                # If there is no south magnet in this row or column, return -1
                if row_south_magnets[i] == 0 or col_south_magnets[j] == 0:
                    return -1
                # If there is a black cell in this row or column, return -1
                for k, l in black_cells:
                    if i == k or j == l:
                        return -1

    # Return the minimum number of north magnets required
    return north_magnets


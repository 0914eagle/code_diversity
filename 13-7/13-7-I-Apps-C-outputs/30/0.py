
def count_monotonic_subgrids(grid):
    rows, cols = len(grid), len(grid[0])
    subgrids = 0
    for row in range(rows):
        for col in range(cols):
            subgrid = grid[row][col]
            if subgrid not in grid[row] or subgrid not in [row[col] for row in grid]:
                continue
            subgrids += 1
    return subgrids


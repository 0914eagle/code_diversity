
def monotonic_subgrids(grid):
    rows, cols = len(grid), len(grid[0])
    subgrids = 0
    for row in range(rows):
        for col in range(cols):
            curr = grid[row][col]
            for i in range(row, rows):
                if grid[i][col] > curr:
                    break
                for j in range(col, cols):
                    if grid[row][j] > curr:
                        break
                    subgrids += 1
    return subgrids



def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        for i in range(len(subgrid) - 1):
            if subgrid[i] > subgrid[i + 1]:
                return False
        return True

    def count_subgrids(grid, rows, cols):
        nonempty_subgrids = 0
        for row in range(rows):
            for col in range(cols):
                subgrid = []
                for i in range(rows):
                    for j in range(cols):
                        if i in rows and j in cols:
                            subgrid.append(grid[i][j])
                if is_monotonic(subgrid):
                    nonempty_subgrids += 1
        return nonempty_subgrids

    rows = len(grid)
    cols = len(grid[0])
    return count_subgrids(grid, rows, cols)


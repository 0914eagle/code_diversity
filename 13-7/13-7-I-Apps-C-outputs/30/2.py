
def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        for i in range(len(subgrid) - 1):
            if subgrid[i] > subgrid[i + 1]:
                return False
        return True

    def count_subgrids(grid, r, c):
        nonlocal count
        if r == 0 or c == 0:
            return

        for i in range(r):
            for j in range(c):
                subgrid = []
                for ii in range(i, r):
                    for jj in range(j, c):
                        subgrid.append(grid[ii][jj])
                if is_monotonic(subgrid):
                    count += 1

        count_subgrids(grid, r - 1, c)
        count_subgrids(grid, r, c - 1)

    count = 0
    count_subgrids(grid, len(grid), len(grid[0]))
    return count


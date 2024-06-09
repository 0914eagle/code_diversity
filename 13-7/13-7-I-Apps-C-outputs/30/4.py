
def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        for i in range(len(subgrid) - 1):
            if subgrid[i] > subgrid[i + 1]:
                return False
        return True

    def count_subgrids(grid, r, c):
        non_empty_subgrids = 0
        for i in range(r):
            for j in range(c):
                subgrid = []
                for k in range(i, r):
                    for l in range(j, c):
                        subgrid.append(grid[k][l])
                if is_monotonic(subgrid):
                    non_empty_subgrids += 1
        return non_empty_subgrids

    return count_subgrids(grid, len(grid), len(grid[0]))


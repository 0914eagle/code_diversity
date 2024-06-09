
def count_monotonic_subgrids(grid):
    def is_monotonic(subgrid):
        for i in range(len(subgrid) - 1):
            if subgrid[i] > subgrid[i + 1]:
                return False
        return True

    def count_subgrids(row_start, col_start, row_end, col_end):
        if row_start > row_end or col_start > col_end:
            return 0
        if row_start == row_end and col_start == col_end:
            return 1 if is_monotonic(grid[row_start][col_start:col_end + 1]) else 0
        return (count_subgrids(row_start, col_start, row_end, col_end - 1) +
                count_subgrids(row_start, col_start + 1, row_end, col_end) +
                count_subgrids(row_start + 1, col_start, row_end, col_end))

    return count_subgrids(0, 0, len(grid) - 1, len(grid[0]) - 1)


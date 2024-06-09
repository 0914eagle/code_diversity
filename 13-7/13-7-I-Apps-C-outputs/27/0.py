
def solve(n, m, k, a):
    # Initialize variables
    rows, cols = [], []
    for i in range(n):
        rows.append([])
        for j in range(m):
            rows[i].append(a[i][j])
            if a[i][j] == 1:
                cols.append([i, j])

    # Check if the table is already a rectangle
    if len(cols) == m:
        return 0

    # Check if it is possible to form a rectangle with at most k cells changed
    if len(cols) + k < m:
        return -1

    # Find the minimum number of cells that need to be changed
    min_cells = m - len(cols)
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and rows[i][j] == 1:
                min_cells += 1
                if min_cells > k:
                    return -1

    return min_cells


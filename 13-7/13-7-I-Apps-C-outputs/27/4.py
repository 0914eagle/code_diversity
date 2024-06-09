
def solve(n, m, k, a):
    # Initialize variables
    rows, cols = {}, {}
    for i in range(n):
        for j in range(m):
            val = a[i][j]
            if val not in rows:
                rows[val] = []
            rows[val].append(i)
            if val not in cols:
                cols[val] = []
            cols[val].append(j)

    # Check if it is possible to change at most k cells
    if k > n * m:
        return -1

    # Initialize the number of cells to change
    cells_to_change = 0

    # Iterate over the rows
    for val in rows:
        row = rows[val]
        if len(row) == 1:
            continue
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                if row[i] != row[j]:
                    cells_to_change += 1
                    if cells_to_change > k:
                        return -1
                    row[i] = row[j] = max(row[i], row[j])

    # Iterate over the columns
    for val in cols:
        col = cols[val]
        if len(col) == 1:
            continue
        for i in range(len(col) - 1):
            for j in range(i + 1, len(col)):
                if col[i] != col[j]:
                    cells_to_change += 1
                    if cells_to_change > k:
                        return -1
                    col[i] = col[j] = max(col[i], col[j])

    return cells_to_change


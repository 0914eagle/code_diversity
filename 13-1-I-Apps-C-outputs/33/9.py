
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]

    # Fill the table with the given values
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]

    # Check if the table meets the requirement
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i][j-1] or table[i][j] != table[i-1][j] or table[i][j] != table[i-1][j-1]:
                    # Check if it's possible to change the value of the cell
                    if k > 0:
                        table[i][j] = 0
                        changed_cells += 1
                        k -= 1
                    else:
                        return -1

    return changed_cells



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
                if table[i][j] == table[i][j-1] and table[i][j] == table[i][j+1] and table[i][j] == table[i-1][j] and table[i][j] == table[i+1][j]:
                    # Check if the connected component forms a rectangle
                    rect_area = 0
                    for ii in range(i, rows):
                        for jj in range(j, cols):
                            if table[ii][jj] == table[i][j]:
                                rect_area += 1
                            else:
                                break
                    if rect_area == (i - i + 1) * (j - j + 1):
                        continue

                # Change the value of the cell if it's not part of a connected component or doesn't form a rectangle
                if changed_cells < k:
                    table[i][j] = 0
                    changed_cells += 1

    # Check if the table meets the requirement after changing the values
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] == table[i][j-1] and table[i][j] == table[i][j+1] and table[i][j] == table[i-1][j] and table[i][j] == table[i+1][j]:
                    # Check if the connected component forms a rectangle
                    rect_area = 0
                    for ii in range(i, rows):
                        for jj in range(j, cols):
                            if table[ii][jj] == table[i][j]:
                                rect_area += 1
                            else:
                                break
                    if rect_area == (i - i + 1) * (j - j + 1):
                        continue

                # If the table doesn't meet the requirement after changing the values, return -1
                return -1

    # If the table meets the requirement after changing the values, return the number of changed cells
    return changed_cells


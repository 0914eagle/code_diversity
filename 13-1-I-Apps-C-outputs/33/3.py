
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]

    # Fill the table with the given values
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # If the current cell is not zero and is not part of a rectangle, check if it can be part of a rectangle
            if table[i][j] != 0 and table[i][j] != 1:
                # Check if the current cell can be part of a rectangle in the current row
                if can_form_rectangle_in_row(table, i, j, rows, cols, k):
                    changed_cells += 1
                    table[i][j] = 1

                # Check if the current cell can be part of a rectangle in the current column
                if can_form_rectangle_in_col(table, i, j, rows, cols, k):
                    changed_cells += 1
                    table[i][j] = 1

    # If the number of changed cells is less than or equal to k, return the number of changed cells
    if changed_cells <= k:
        return changed_cells
    else:
        return -1

# Check if the current cell can be part of a rectangle in the current row
def can_form_rectangle_in_row(table, i, j, rows, cols, k):
    # Initialize variables
    count = 0
    start_index = j
    end_index = j

    # Loop through the row and count the number of consecutive cells with the same value as the current cell
    while start_index >= 0 and table[i][start_index] == table[i][j]:
        count += 1
        start_index -= 1
    while end_index < cols and table[i][end_index] == table[i][j]:
        count += 1
        end_index += 1

    # If the number of consecutive cells is greater than or equal to the number of rows, return True
    if count >= rows:
        return True

    # Otherwise, return False
    return False

# Check if the current cell can be part of a rectangle in the current column
def can_form_rectangle_in_col(table, i, j, rows, cols, k):
    # Initialize variables
    count = 0
    start_index = i
    end_index = i

    # Loop through the column and count the number of consecutive cells with the same value as the current cell
    while start_index >= 0 and table[start_index][j] == table[i][j]:
        count += 1
        start_index -= 1
    while end_index < rows and table[end_index][j] == table[i][j]:
        count += 1
        end_index += 1

    # If the number of consecutive cells is greater than or equal to the number of columns, return True
    if count >= cols:
        return True

    # Otherwise, return False
    return False


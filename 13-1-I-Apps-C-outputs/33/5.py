
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
                # Check if the current cell can be part of a rectangle in the current column
                if can_form_rectangle_in_col(table, i, j, rows, cols, k):
                    changed_cells += 1

    # Return the minimum number of cells that need to be changed
    return changed_cells

# Check if the current cell can be part of a rectangle in the current row
def can_form_rectangle_in_row(table, i, j, rows, cols, k):
    # Initialize variables
    start_index, end_index = j, j
    count = 1

    # Loop through the row and check if the current cell can be part of a rectangle
    while start_index >= 0 and table[i][start_index] == table[i][j]:
        start_index -= 1
        count += 1

    while end_index < cols and table[i][end_index] == table[i][j]:
        end_index += 1
        count += 1

    # If the current cell can be part of a rectangle, check if the rectangle is valid
    if start_index >= 0 and end_index < cols and count > 1:
        # Calculate the area of the rectangle
        area = (end_index - start_index) * count

        # Check if the rectangle is valid
        if area <= k:
            # Change the values of the cells in the rectangle
            for x in range(start_index, end_index + 1):
                for y in range(i, i + count):
                    table[y][x] = 1
            return True

    return False

# Check if the current cell can be part of a rectangle in the current column
def can_form_rectangle_in_col(table, i, j, rows, cols, k):
    # Initialize variables
    start_index, end_index = i, i
    count = 1

    # Loop through the column and check if the current cell can be part of a rectangle
    while start_index >= 0 and table[start_index][j] == table[i][j]:
        start_index -= 1
        count += 1

    while end_index < rows and table[end_index][j] == table[i][j]:
        end_index += 1
        count += 1

    # If the current cell can be part of a rectangle, check if the rectangle is valid
    if start_index >= 0 and end_index < rows and count > 1:
        # Calculate the area of the rectangle
        area = (end_index - start_index) * count

        # Check if the rectangle is valid
        if area <= k:
            # Change the values of the cells in the rectangle
            for x in range(start_index, end_index + 1):
                for y in range(j, j + count):
                    table[x][y] = 1
            return True

    return False



def max_clean_rows(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    clean_rows = 0
    dirty_cols = [0] * cols

    # Iterate over each row
    for i in range(rows):
        # Iterate over each column
        for j in range(cols):
            # If the current square is clean and the column is dirty, make the column dirty
            if grid[i][j] == "0" and dirty_cols[j] == 0:
                dirty_cols[j] = 1
            # If the current square is dirty and the column is clean, make the column clean
            elif grid[i][j] == "1" and dirty_cols[j] == 1:
                dirty_cols[j] = 0

        # If all squares in the current row are clean, increase the number of clean rows
        if all(grid[i] == "0" for i in range(rows)):
            clean_rows += 1

    return clean_rows


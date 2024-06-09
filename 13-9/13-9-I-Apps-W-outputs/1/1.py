
def max_rows_clean(n, grid):
    # Initialize the number of rows cleaned to 0
    rows_cleaned = 0

    # Iterate through each column of the grid
    for col in range(n):
        # Initialize the number of rows cleaned in this column to 0
        rows_cleaned_in_col = 0

        # Iterate through each row of the grid
        for row in range(n):
            # Check if the current square is clean
            if grid[row][col] == "0":
                # If the current square is clean, increment the number of rows cleaned in this column
                rows_cleaned_in_col += 1

        # Check if the number of rows cleaned in this column is equal to the number of rows in the grid
        if rows_cleaned_in_col == n:
            # If so, increment the total number of rows cleaned
            rows_cleaned += 1

    # Return the total number of rows cleaned
    return rows_cleaned



def solve(n, grid):
    # Initialize the maximum number of rows that can be made clean
    max_clean_rows = 0
    # Loop through each column of the grid
    for col in range(n):
        # Initialize the number of clean rows in the current column
        clean_rows = 0
        # Loop through each row of the grid
        for row in range(n):
            # Check if the current square is clean
            if grid[row][col] == "1":
                # Increment the number of clean rows in the current column
                clean_rows += 1
        # Update the maximum number of rows that can be made clean
        max_clean_rows = max(max_clean_rows, clean_rows)
    # Return the maximum number of rows that can be made clean
    return max_clean_rows


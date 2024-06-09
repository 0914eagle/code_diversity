
def max_clean_rows(n, room):
    # Initialize the maximum number of clean rows to 0
    max_clean = 0
    # Loop through each column of the grid
    for col in range(n):
        # Initialize the number of clean rows in this column to 0
        clean_rows = 0
        # Loop through each row of the grid
        for row in range(n):
            # If the square in this row and column is clean, increment the number of clean rows
            if room[row][col] == "1":
                clean_rows += 1
        # If the number of clean rows in this column is greater than the maximum, update the maximum
        if clean_rows > max_clean:
            max_clean = clean_rows
    # Return the maximum number of clean rows
    return max_clean


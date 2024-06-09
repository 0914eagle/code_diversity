
def solve(n, room):
    # Initialize the maximum number of clean rows to 0
    max_clean_rows = 0
    # Loop through each column of the room
    for col in range(n):
        # Initialize the number of clean rows in this column to 0
        clean_rows = 0
        # Loop through each row in the column
        for row in range(n):
            # If the square is clean, increment the number of clean rows
            if room[row][col] == "1":
                clean_rows += 1
        # If the number of clean rows in this column is greater than the maximum, update the maximum
        if clean_rows > max_clean_rows:
            max_clean_rows = clean_rows
    # Return the maximum number of clean rows
    return max_clean_rows


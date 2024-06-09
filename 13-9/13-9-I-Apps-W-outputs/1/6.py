
def solve(n, room):
    # Initialize the maximum number of clean rows to 0
    max_clean_rows = 0
    # Loop through each column of the room
    for col in range(n):
        # Initialize the number of clean rows in this column to 0
        clean_rows = 0
        # Loop through each row in the column
        for row in range(n):
            # Check if the current square is clean
            if room[row][col] == "1":
                # Increment the number of clean rows in this column
                clean_rows += 1
        # Update the maximum number of clean rows if necessary
        max_clean_rows = max(max_clean_rows, clean_rows)
    # Return the maximum number of clean rows
    return max_clean_rows


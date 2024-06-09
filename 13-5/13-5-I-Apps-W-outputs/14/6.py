
def max_clean_rows(n, grid):
    # Initialize the number of clean rows to 0
    num_clean_rows = 0
    
    # Loop through each column of the grid
    for col in range(n):
        # Initialize the number of clean squares in this column to 0
        num_clean_squares = 0
        
        # Loop through each row of the grid
        for row in range(n):
            # Check if the square at the current row and column is clean
            if grid[row][col] == "1":
                # Increment the number of clean squares in this column
                num_clean_squares += 1
        
        # Check if the number of clean squares in this column is equal to the number of rows in the grid
        if num_clean_squares == n:
            # Increment the number of clean rows
            num_clean_rows += 1
    
    # Return the maximum number of clean rows
    return num_clean_rows



def solve(n, grid):
    # Initialize the maximum number of rows that can be made completely clean
    max_rows = 0
    
    # Loop through each column of the grid
    for col in range(n):
        # Initialize the number of clean rows in this column
        num_clean_rows = 0
        
        # Loop through each row in the column
        for row in range(n):
            # If the square is clean, increment the number of clean rows
            if grid[row][col] == "1":
                num_clean_rows += 1
        
        # If the number of clean rows in this column is greater than the maximum number of rows that can be made completely clean, update the maximum number of rows
        if num_clean_rows > max_rows:
            max_rows = num_clean_rows
    
    # Return the maximum number of rows that can be made completely clean
    return max_rows


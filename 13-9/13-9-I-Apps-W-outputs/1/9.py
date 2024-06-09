
def max_clean_rows(n, grid):
    # Initialize the number of clean rows to 0
    num_clean_rows = 0
    
    # Loop through each column of the grid
    for col in range(n):
        # Initialize a flag to keep track of whether the column is clean or dirty
        is_clean = True
        
        # Loop through each row of the column
        for row in range(n):
            # Check if the current square is clean
            if grid[row][col] == "0":
                # If the square is dirty, set the is_clean flag to False
                is_clean = False
                break
        
        # If the column is clean, increment the number of clean rows
        if is_clean:
            num_clean_rows += 1
    
    # Return the number of clean rows
    return num_clean_rows


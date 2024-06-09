
def solve(grid):
    # Get the number of rows and columns
    n_rows, n_cols = len(grid), len(grid[0])
    
    # Initialize the rating variable
    rating = 0
    
    # Iterate over each row
    for i in range(n_rows):
        # Initialize the number of blank columns in the current row
        n_blank = 0
        
        # Iterate over each column in the current row
        for j in range(n_cols):
            # If the current character is a blank, increase the number of blank columns
            if grid[i][j] == "_":
                n_blank += 1
            # If the current character is a dollar sign and the previous character is also a dollar sign, increase the rating
            elif grid[i][j] == "$" and grid[i][j-1] == "$":
                rating += 1
    
    # Return the rating
    return rating



def solve(grid):
    # Convert the grid to a numpy array for easier manipulation
    grid = np.array(grid)
    
    # Initialize a flag to indicate if the grid has changed
    changed = True
    
    # While the grid has changed, repeat the following operations
    while changed:
        # Find the rows and columns that only contain white squares
        rows, cols = np.where(grid == ".")
        
        # If there are no rows or columns with only white squares, break the loop
        if len(rows) == 0 and len(cols) == 0:
            break
        
        # Remove the rows and columns with only white squares
        grid = np.delete(grid, rows, axis=0)
        grid = np.delete(grid, cols, axis=1)
        
        # Set the flag to indicate that the grid has changed
        changed = True
    
    # Return the final state of the grid
    return grid


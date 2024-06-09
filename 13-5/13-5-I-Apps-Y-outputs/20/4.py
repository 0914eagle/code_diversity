
def solve(grid):
    # Convert the grid to a numpy array for easier manipulation
    grid = np.array(grid)
    
    # Find the indices of the rows and columns that consist only of white squares
    row_indices, col_indices = np.where(grid == ".")
    
    # Remove the rows and columns that consist only of white squares
    grid = np.delete(grid, row_indices, axis=0)
    grid = np.delete(grid, col_indices, axis=1)
    
    # Return the final state of the grid
    return grid


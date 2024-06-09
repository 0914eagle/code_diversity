
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Initialize a list to store the rows and columns of the cells to be purified
    rows, cols = [], []
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # Check if the current cell is a particularly more evil cell
            if grid[i][j] == 'E':
                # Add the current cell's row and column to the lists of rows and columns to be purified
                rows.append(i)
                cols.append(j)
    
    # Sort the lists of rows and columns to be purified
    rows.sort()
    cols.sort()
    
    # Loop through each row to be purified
    for i in rows:
        # Loop through each column to be purified
        for j in cols:
            # Check if the current cell has not yet been purified
            if grid[i][j] == 'E':
                # Cast the "Purification" spell on the current cell
                grid[i][j] = '.'
                # Increment the number of purification spells to be cast
                num_spells += 1
    
    # Return the number of purification spells to be cast
    return num_spells


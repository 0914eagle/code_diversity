
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # If the current cell is a particularly more evil cell, skip it
            if grid[i][j] == 'E':
                continue
            # Otherwise, cast a purification spell on the current cell
            num_spells += 1
            # Loop through each row and column of the grid
            for k in range(len(grid)):
                # If the current cell is not a particularly more evil cell and is not the current cell, purify it
                if grid[k][j] != 'E' and (i != k or j != k):
                    grid[k][j] = '.'
    
    # Return the number of purification spells to be cast
    return num_spells


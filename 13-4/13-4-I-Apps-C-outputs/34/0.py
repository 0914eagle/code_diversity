
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # If the current cell is an evil cell and has not been purified yet,
            if grid[i][j] == "E" and grid[i][j] != ".":
                # Cast the purification spell on the current cell
                grid[i][j] = "."
                # Increment the number of purification spells to be cast
                num_spells += 1
                # Loop through the rows and columns of the grid
                for k in range(len(grid)):
                    # If the current cell is in the same row or column as the current cell and is an evil cell,
                    if (grid[k][j] == "E" and grid[k][j] != ".") or (grid[i][k] == "E" and grid[i][k] != "."):
                        # Cast the purification spell on the current cell
                        grid[k][j] = "."
                        grid[i][k] = "."
                        # Increment the number of purification spells to be cast
                        num_spells += 1
    
    # Return the number of purification spells to be cast
    return num_spells


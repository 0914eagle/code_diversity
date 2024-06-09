
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # If the current cell is evil and not a particularly more evil cell, purify it
            if grid[i][j] == "E" and grid[i][j] != ".":
                num_spells += 1
                # Purify the current cell and all cells in the same row and column
                for k in range(len(grid)):
                    if grid[k][j] == "E" and grid[k][j] != ".":
                        grid[k][j] = "."
                for k in range(len(grid[i])):
                    if grid[i][k] == "E" and grid[i][k] != ".":
                        grid[i][k] = "."
    
    # If all cells have been purified, return the number of purification spells cast
    if "E" not in "".join(grid):
        return num_spells
    # Otherwise, return -1
    else:
        return -1


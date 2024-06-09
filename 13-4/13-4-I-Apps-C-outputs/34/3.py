
def purify_cells(grid):
    # Initialize the number of purification spells to be cast
    num_spells = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[i])):
            # If the current cell is evil and not a particularly more evil cell, cast a purification spell on it
            if grid[i][j] == "E" and grid[i][j] != ".":
                num_spells += 1
                # Cast the purification spell on the current cell
                grid[i][j] = "."
                # Loop through the rows and columns of the grid
                for k in range(len(grid)):
                    # If the current cell is in the same row or column as the current cell, and it is not a particularly more evil cell, purify it
                    if grid[k][j] == "E" and grid[k][j] != ".":
                        grid[k][j] = "."
    
    # If all cells have been purified, return the number of purification spells cast
    if "E" not in "".join(grid):
        return num_spells
    # Otherwise, return -1
    else:
        return -1


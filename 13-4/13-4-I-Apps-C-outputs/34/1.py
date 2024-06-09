
def purify_cells(grid):
    # Initialize the number of spells to cast and the list of cells to purify
    num_spells = 0
    cells_to_purify = []
    
    # Loop through each row and column of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is evil and not already purified, add it to the list of cells to purify
            if grid[i][j] == "E" and [i, j] not in cells_to_purify:
                cells_to_purify.append([i, j])
    
    # While there are still cells to purify
    while cells_to_purify:
        # Get the first cell to purify from the list
        cell = cells_to_purify.pop(0)
        # Cast the "Purification" spell on the cell
        grid[cell[0]][cell[1]] = "."
        # Add the cells in the same row and column as the current cell to the list of cells to purify
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "E" and (i == cell[0] or j == cell[1]):
                    cells_to_purify.append([i, j])
        # Increment the number of spells to cast
        num_spells += 1
    
    # If all cells have been purified, return the number of spells to cast
    if "E" not in "".join(grid):
        return num_spells
    # Otherwise, return -1
    else:
        return -1


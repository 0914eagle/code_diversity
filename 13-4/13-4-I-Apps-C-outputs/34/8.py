
def purify_cells(grid):
    # Initialize the number of spells to cast and the list of cells to purify
    num_spells = 0
    cells_to_purify = []

    # Loop through each row and column
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is evil and not already purified, add it to the list of cells to purify
            if grid[i][j] == "E" and [i, j] not in cells_to_purify:
                cells_to_purify.append([i, j])

    # While there are still cells to purify
    while cells_to_purify:
        # Get the first cell to purify from the list
        current_cell = cells_to_purify.pop(0)

        # Add the current cell to the list of purified cells
        purified_cells = [current_cell]

        # Loop through the rows and columns of the current cell
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If the current cell is in the same row or column as the current cell and is evil and not already purified, add it to the list of cells to purify
                if (i, j) in [(current_cell[0] + x, current_cell[1] + y) for x in range(-1, 2) for y in range(-1, 2)] and grid[i][j] == "E" and [i, j] not in purified_cells and [i, j] not in cells_to_purify:
                    cells_to_purify.append([i, j])
                    purified_cells.append([i, j])

        # Increment the number of spells to cast
        num_spells += 1

    # If all cells have been purified, return the number of spells to cast
    if len(purified_cells) == len(grid) * len(grid[0]):
        return num_spells

    # Otherwise, return -1
    return -1



def purify_cells(grid):
    # Initialize the number of spells to cast and the list of cells to purify
    num_spells = 0
    cells_to_purify = []

    # Loop through each row and column
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current cell is evil and not a particularly more evil cell, add it to the list of cells to purify
            if grid[row][col] == "E" and grid[row][col] != ".":
                cells_to_purify.append((row, col))

    # While there are still cells to purify
    while cells_to_purify:
        # Pop the first cell from the list of cells to purify
        row, col = cells_to_purify.pop(0)

        # Cast the "Purification" spell on the current cell
        grid[row][col] = "."

        # Add the cells in the same row and column as the current cell to the list of cells to purify
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "E" and grid[i][j] != ".":
                    cells_to_purify.append((i, j))

        # Increment the number of spells to cast
        num_spells += 1

    # If all cells have been purified, return the number of spells to cast
    if "E" not in "".join(grid):
        return num_spells

    # Otherwise, return -1
    return -1


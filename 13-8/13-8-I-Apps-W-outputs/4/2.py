
def cake_eater(grid):
    # Initialize variables
    rows = len(grid)
    cols = len(grid[0])
    max_cells = 0

    # Iterate over each row
    for i in range(rows):
        # Check if the row contains any evil strawberries
        if 'S' in grid[i]:
            # If the row contains evil strawberries, iterate over each column
            for j in range(cols):
                # Check if the column contains any evil strawberries
                if 'S' in [row[j] for row in grid]:
                    # If the column contains evil strawberries, iterate over each cell
                    for k in range(rows):
                        # Check if the cell has not been eaten before
                        if grid[k][j] == '.':
                            # If the cell has not been eaten before, eat it and update the maximum number of cells eaten
                            grid[k][j] = 'E'
                            max_cells += 1

    # Return the maximum number of cells eaten
    return max_cells


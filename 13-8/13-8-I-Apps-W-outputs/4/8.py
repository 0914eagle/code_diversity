
def cake_eater(grid):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    total_cells = rows * cols
    eaten_cells = 0
    max_eaten_cells = 0

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # Check if the cell has an evil strawberry
            if grid[i][j] == 'S':
                # Calculate the number of cells in the row and column that have not been eaten
                row_cells = sum([1 if grid[i][k] == '.' else 0 for k in range(cols)])
                col_cells = sum([1 if grid[k][j] == '.' else 0 for k in range(rows)])

                # Update the maximum number of cells that can be eaten
                max_eaten_cells = max(max_eaten_cells, row_cells + col_cells)

    return max_eaten_cells


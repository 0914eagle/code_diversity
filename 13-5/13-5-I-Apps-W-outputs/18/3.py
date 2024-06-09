
def solve(grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
    # Initialize the list of operations to be performed
    operations = []
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell contains an even number of coins, increment the number of even cells
            if grid[i][j] % 2 == 0:
                num_even_cells += 1
            # If the cell contains an odd number of coins, find a vertically or horizontally adjacent cell with an even number of coins
            elif grid[i][j] % 2 == 1:
                # Find the row and column indices of the cell
                row, col = i, j
                # Loop through the rows and columns above, below, to the left, and to the right of the current cell
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        # If the row and column indices are valid and the cell contains an even number of coins, add the operation to the list of operations
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] % 2 == 0:
                            operations.append([row, col, r, c])
                            # Break out of the loops once an even cell has been found
                            break
                    if len(operations) > 0:
                        break
                # If no even cell was found, the number of even cells remains the same
                else:
                    num_even_cells += 1
    # Return the number of even cells and the list of operations
    return num_even_cells, operations


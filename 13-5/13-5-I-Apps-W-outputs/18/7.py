
def solve(grid):
    # Initialize the number of even cells to 0
    even_cells = 0
    # Initialize the number of operations to 0
    operations = 0
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the current row
        for j in range(len(grid[i])):
            # Check if the current cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # Increment the number of even cells
                even_cells += 1
            # Check if the current cell is not in the last row or column
            if i != len(grid) - 1 and j != len(grid[i]) - 1:
                # Check if the cell below and to the right of the current cell contains an even number of coins
                if grid[i+1][j+1] % 2 == 0:
                    # Increment the number of operations
                    operations += 1
                    # Move the coin from the current cell to the cell below and to the right
                    grid[i+1][j+1] += grid[i][j]
                    grid[i][j] = 0
    # Return the number of even cells and the number of operations
    return even_cells, operations


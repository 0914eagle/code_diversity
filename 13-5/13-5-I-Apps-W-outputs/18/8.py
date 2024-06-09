
def solve_problem(grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
    # Initialize the sequence of operations to be performed
    operations = []
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the current row
        for j in range(len(grid[i])):
            # Check if the current cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # Increment the number of even cells
                num_even_cells += 1
            # Check if the current cell is not the last cell in the row
            if j < len(grid[i]) - 1:
                # Check if the cell to the right of the current cell contains an even number of coins
                if grid[i][j+1] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                    # Add the operation of moving a coin from the current cell to the cell to the right to the sequence of operations
                    operations.append([i, j, i, j+1])
            # Check if the current cell is not the last cell in the column
            if i < len(grid) - 1:
                # Check if the cell below the current cell contains an even number of coins
                if grid[i+1][j] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                    # Add the operation of moving a coin from the current cell to the cell below to the sequence of operations
                    operations.append([i, j, i+1, j])
    # Return the number of even cells and the sequence of operations
    return num_even_cells, operations


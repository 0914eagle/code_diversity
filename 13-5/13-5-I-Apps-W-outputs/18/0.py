
def solve_problem(grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
    # Initialize the number of operations to 0
    num_operations = 0
    # Initialize the list of operations to be performed
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
                # Check if the cell to the right contains an odd number of coins
                if grid[i][j+1] % 2 == 1:
                    # Increment the number of operations
                    num_operations += 1
                    # Add the current cell and the cell to the right to the list of operations
                    operations.append([i, j, i, j+1])
            # Check if the current cell is not the last cell in the column
            if i < len(grid) - 1:
                # Check if the cell below contains an odd number of coins
                if grid[i+1][j] % 2 == 1:
                    # Increment the number of operations
                    num_operations += 1
                    # Add the current cell and the cell below to the list of operations
                    operations.append([i, j, i+1, j])

    # Return the number of even cells and the list of operations
    return num_even_cells, operations


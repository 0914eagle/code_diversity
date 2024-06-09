
def solve_problem(grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
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
            # Check if the current cell is not in the last row or column
            if i != len(grid) - 1 and j != len(grid[i]) - 1:
                # Check if the cell below and to the right of the current cell contains an even number of coins
                if grid[i+1][j+1] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                    # Add the current cell and the cell below and to the right of the current cell to the list of operations
                    operations.append([i, j, i+1, j+1])
            # Check if the current cell is not in the last row
            if i != len(grid) - 1:
                # Check if the cell below the current cell contains an even number of coins
                if grid[i+1][j] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                    # Add the current cell and the cell below the current cell to the list of operations
                    operations.append([i, j, i+1, j])
            # Check if the current cell is not in the last column
            if j != len(grid[i]) - 1:
                # Check if the cell to the right of the current cell contains an even number of coins
                if grid[i][j+1] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                    # Add the current cell and the cell to the right of the current cell to the list of operations
                    operations.append([i, j, i, j+1])
    # Return the number of even cells and the list of operations
    return num_even_cells, operations


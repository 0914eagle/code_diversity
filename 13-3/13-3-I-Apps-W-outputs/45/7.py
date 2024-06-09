
def solve(grid):
    # Initialize the number of even cells to 0
    num_even_cells = 0
    # Initialize the sequence of operations to be returned
    sequence = []
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # Increment the number of even cells
                num_even_cells += 1
            # Check if the current cell is not in the top row or bottom row
            if i > 0 and i < len(grid) - 1:
                # Check if the cell above the current cell contains an even number of coins
                if grid[i - 1][j] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                # Check if the cell below the current cell contains an even number of coins
                if grid[i + 1][j] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
            # Check if the current cell is not in the left column or right column
            if j > 0 and j < len(grid[0]) - 1:
                # Check if the cell to the left of the current cell contains an even number of coins
                if grid[i][j - 1] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
                # Check if the cell to the right of the current cell contains an even number of coins
                if grid[i][j + 1] % 2 == 0:
                    # Increment the number of even cells
                    num_even_cells += 1
    # Return the number of even cells and the sequence of operations
    return num_even_cells, sequence


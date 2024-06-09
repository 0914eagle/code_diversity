
def solve_coin_problem(grid):
    # Initialize variables
    max_even_cells = 0
    operations = []

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # Add the cell to the list of cells with an even number of coins
                max_even_cells += 1
                operations.append([i, j])
            # Check if the cell contains an odd number of coins
            elif grid[i][j] % 2 == 1:
                # Check if the cell has a vertically or horizontally adjacent cell with an even number of coins
                for k in range(len(grid)):
                    for l in range(len(grid[0])):
                        if grid[k][l] % 2 == 0 and (k == i or l == j):
                            # Add the cell to the list of cells with an even number of coins
                            max_even_cells += 1
                            operations.append([i, j])

    # Return the list of operations that maximizes the number of cells with an even number of coins
    return operations


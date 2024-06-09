
def solve_coin_problem(grid):
    # Initialize variables
    max_even_cells = 0
    operations = []

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell contains an even number of coins, add it to the list of even cells
            if grid[i][j] % 2 == 0:
                max_even_cells += 1
            # If the cell contains an odd number of coins, try to move a coin to an adjacent cell
            else:
                # Check if the cell has any adjacent cells with an even number of coins
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        # If the adjacent cell is within the bounds of the grid and contains an even number of coins, move a coin to it
                        if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] % 2 == 0:
                            grid[i][j] -= 1
                            grid[k][l] += 1
                            operations.append([i+1, j+1, k+1, l+1])
                            break

    # Return the maximum number of even cells and the list of operations
    return max_even_cells, operations


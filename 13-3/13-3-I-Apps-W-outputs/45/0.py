
def solve_coin_problem(grid):
    # Initialize variables
    max_even_cells = 0
    operations = []

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell contains an even number of coins, increment the maximum number of even cells
            if grid[i][j] % 2 == 0:
                max_even_cells += 1
            # If the cell contains an odd number of coins, try to move a coin to an adjacent cell
            else:
                # Check if the cell has a coin that can be moved to an adjacent cell
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]) and grid[i+di][j+dj] % 2 == 0:
                            # Move the coin to the adjacent cell and increment the maximum number of even cells
                            grid[i+di][j+dj] += 1
                            grid[i][j] -= 1
                            max_even_cells += 1
                            operations.append([i, j, i+di, j+dj])
                            break

    # Return the maximum number of even cells and the list of operations
    return max_even_cells, operations


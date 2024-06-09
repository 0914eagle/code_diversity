
def solve(grid):
    # Initialize variables
    max_even_cells = 0
    operations = []

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current cell contains an even number of coins
            if grid[i][j] % 2 == 0:
                # If the current cell contains an even number of coins, check if moving a coin to a vertically or horizontally adjacent cell will result in an even number of coins in that cell
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        # Check if the adjacent cell is valid and contains at least one coin
                        if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] > 0:
                            # Move a coin from the current cell to the adjacent cell
                            grid[i][j] -= 1
                            grid[k][l] += 1
                            # Check if the number of even cells has increased
                            if grid[k][l] % 2 == 0 and grid[i][j] % 2 == 1:
                                max_even_cells += 1
                                operations.append([i+1, j+1, k+1, l+1])
                            # Move the coin back to the current cell
                            grid[i][j] += 1
                            grid[k][l] -= 1

    return [max_even_cells, operations]


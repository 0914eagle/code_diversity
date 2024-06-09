
def count_ship_placements(n, k, grid, ship_sizes):
    # Initialize a 2D array to store the number of ways to place each ship
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # Loop through each row of the grid
    for i in range(n):
        # Loop through each column of the grid
        for j in range(n):
            # If the current cell is not blocked by a shot
            if grid[i][j] == '.':
                # Loop through each ship size
                for ship_size in ship_sizes:
                    # If the current cell is not at the end of the grid and the ship fits in the remaining cells
                    if i + ship_size <= n and j + ship_size <= n:
                        # Add the number of ways to place the ship to the current cell
                        dp[i + ship_size][j + ship_size] += dp[i][j]

    # Return the number of ways to place all k ships
    return dp[n][n]


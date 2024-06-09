
def count_ship_placements(n, k, grid, ship_sizes):
    # Initialize a 2D array to store the number of ways to place each ship
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # Loop through each ship
    for ship_size in ship_sizes:
        for i in range(n):
            for j in range(n):
                # Check if the current cell is empty and the ship fits in the grid
                if grid[i][j] == "." and i + ship_size <= n and j + ship_size <= n:
                    # Update the number of ways to place the ship
                    dp[i + ship_size][j + ship_size] += dp[i][j]

    # Return the number of ways to place all k ships
    return dp[n][n]


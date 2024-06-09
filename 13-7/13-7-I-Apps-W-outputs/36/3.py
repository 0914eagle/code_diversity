
def count_ship_placements(n, k, grid, ship_sizes):
    # Initialize a 2D array to store the number of ways to place each ship
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1

    # Loop through each row of the grid
    for i in range(n):
        # Loop through each column of the grid
        for j in range(n):
            # Check if the current square is occupied by a ship
            if grid[i][j] == "X":
                # Loop through each ship
                for ship in range(1, k + 1):
                    # Check if the current ship can be placed in the current square
                    if dp[ship - 1][j] > 0 and (j + ship_sizes[ship - 1] - 1 < n or j - ship_sizes[ship - 1] + 1 >= 0):
                        # Update the number of ways to place the current ship
                        dp[ship][j] += dp[ship - 1][j]

    # Return the number of ways to place all k ships
    return dp[k][n - 1]


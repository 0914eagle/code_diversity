
def battleship(n, k, board, ships):
    # Initialize a 2D array to store the number of ways to place each ship
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # Loop through each ship
    for i in range(k):
        # Get the size of the current ship
        ship_size = ships[i]

        # Loop through each row and column of the board
        for r in range(n):
            for c in range(n):
                # If the current square is not occupied by a ship
                if board[r][c] == ".":
                    # Loop through each direction (horizontal and vertical)
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            # If the current direction is valid and the square is not occupied by a ship
                            if 0 <= r + dr < n and 0 <= c + dc < n and board[r + dr][c + dc] == ".":
                                # Update the number of ways to place the ship
                                dp[r + dr][c + dc] += dp[r][c]

    # Return the number of ways to place all the ships
    return dp[n - 1][n - 1]


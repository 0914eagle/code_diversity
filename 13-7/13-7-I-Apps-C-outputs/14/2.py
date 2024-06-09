
def solve(N, game_state):
    # Initialize the variables
    alice_score = 0
    bob_score = 0
    moves_left = N * N

    # Iterate through the game state
    for i in range(N):
        for j in range(N):
            # Check if the current cell is a dot
            if game_state[i][j] == "*":
                # Check if the dot is connected to the edge of the grid
                if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                    # The dot is connected to the edge, so Alice or Bob can score a point
                    return moves_left
                else:
                    # The dot is not connected to the edge, so check the surrounding cells
                    if game_state[i - 1][j] == "|" and game_state[i + 1][j] == "|" and game_state[i][j - 1] == "-" and game_state[i][j + 1] == "-":
                        # The dot is connected to the edge in all four directions, so Alice or Bob can score a point
                        return moves_left

    # If the function reaches this point, then no dot is connected to the edge, so the game can continue
    return moves_left


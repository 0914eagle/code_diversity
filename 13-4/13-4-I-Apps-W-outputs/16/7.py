
def get_min_pebbles(n):
    # Initialize variables
    mirror_move = False
    current_player = "Mirko"
    pebbles_taken = 0
    other_player_pebbles = 0

    # Iterate through the game
    while n > 0:
        # Determine the current player and their allowed number of pebbles
        if current_player == "Mirko":
            allowed_pebbles = n
        else:
            allowed_pebbles = min(n, 2 * other_player_pebbles)

        # Update the number of pebbles taken and the number of pebbles the other player has
        pebbles_taken += allowed_pebbles
        other_player_pebbles = n - allowed_pebbles

        # Update the current player and mirror move
        current_player = "Slavko" if current_player == "Mirko" else "Mirko"
        mirror_move = not mirror_move

        # If the current player has taken all the pebbles, return the minimum number of pebbles needed for Mirko to win
        if pebbles_taken == n:
            return pebbles_taken - other_player_pebbles

    # If the game has not ended, return the minimum number of pebbles needed for Mirko to win
    return pebbles_taken


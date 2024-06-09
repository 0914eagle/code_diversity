
def get_min_pebbles(n):
    # Initialize variables
    mirror_pebbles = n
    current_player = "Mirko"
    other_player = "Slavko"
    turn = 1
    min_pebbles = 1

    # Play the game
    while mirror_pebbles > 0:
        # Determine the number of pebbles the current player can take
        if current_player == "Mirko":
            max_pebbles = min(n, 2 * turn)
        else:
            max_pebbles = min(mirror_pebbles, 2 * turn)

        # Update the number of pebbles in the heap
        mirror_pebbles -= max_pebbles

        # Switch players
        current_player, other_player = other_player, current_player
        turn += 1

        # Update the minimum number of pebbles
        min_pebbles = max(min_pebbles, max_pebbles)

    return min_pebbles


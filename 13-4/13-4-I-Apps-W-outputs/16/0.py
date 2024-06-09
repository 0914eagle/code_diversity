
def find_min_pebbles(N):
    # Initialize variables
    mirror_pebbles = N
    current_player = "Mirko"
    other_player = "Slavko"
    turn = 1

    # Game loop
    while mirror_pebbles > 0:
        # Determine number of pebbles to take
        if current_player == "Mirko":
            num_pebbles = mirror_pebbles
        else:
            num_pebbles = min(mirror_pebbles, 2 * (N - mirror_pebbles))

        # Update variables
        mirror_pebbles -= num_pebbles
        turn += 1
        current_player, other_player = other_player, current_player

    # Return result
    return N - mirror_pebbles


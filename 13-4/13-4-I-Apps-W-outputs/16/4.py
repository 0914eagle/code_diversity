
def find_min_pebbles(n):
    # Initialize variables
    mirror_pebbles = n
    current_player = "Mirko"
    other_player = "Slavko"
    turn = 1

    # While there are still pebbles in the heap
    while mirror_pebbles > 0:
        # Determine the current player and the number of pebbles they can take
        if current_player == "Mirko":
            num_pebbles = min(mirror_pebbles, n)
        else:
            num_pebbles = min(mirror_pebbles, 2 * (n - turn + 1))

        # Update the number of pebbles in the heap and the turn number
        mirror_pebbles -= num_pebbles
        turn += 1

        # Switch players
        current_player, other_player = other_player, current_player

    # Return the minimum number of pebbles that Mirko must take during his first turn
    return n


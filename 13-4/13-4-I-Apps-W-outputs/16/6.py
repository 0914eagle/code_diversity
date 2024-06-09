
def get_min_pebbles(n):
    # Initialize variables
    mirror_game = True
    pebbles_taken = 0
    pebbles_remaining = n

    # While there are still pebbles remaining in the heap
    while pebbles_remaining > 0:
        # If it is Mirko's turn
        if mirror_game:
            # He can take any number of pebbles between 1 and the number of pebbles remaining in the heap, inclusive
            pebbles_taken = random.randint(1, pebbles_remaining)
            pebbles_remaining -= pebbles_taken
        # If it is Slavko's turn
        else:
            # He can take at most double the number of pebbles taken by Mirko during the previous turn
            pebbles_taken = 2 * pebbles_taken
            pebbles_remaining -= pebbles_taken

        # Flip the mirror game
        mirror_game = not mirror_game

    # Return the minimum number of pebbles that Mirko must take during his first turn
    return pebbles_taken


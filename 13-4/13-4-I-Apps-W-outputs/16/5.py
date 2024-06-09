
def solve(N):
    # Initialize variables
    mirko_turn = True
    pebbles_taken = 0
    pebbles_remaining = N

    # While there are still pebbles remaining in the heap
    while pebbles_remaining > 0:
        # If it's Mirko's turn
        if mirko_turn:
            # Mirko can take any number of pebbles between 1 and the number of pebbles remaining in the heap
            pebbles_taken = random.randint(1, pebbles_remaining)
            pebbles_remaining -= pebbles_taken
        # If it's Slavko's turn
        else:
            # Slavko can take at most double the number of pebbles taken by Mirko during his previous turn
            pebbles_taken = 2 * pebbles_taken
            pebbles_remaining -= pebbles_taken

        # Switch turns
        mirko_turn = not mirko_turn

    # Return the minimum number of pebbles that Mirko must take during his first turn
    return pebbles_taken



def coconut_splat(syllables, num_players):
    # Initialize the hands of each player as folded
    hands = [True] * num_players
    # Initialize the current player as player 1
    current_player = 0
    # Loop until only one player is left
    while len(hands) > 1:
        # Check if the current player has their hands folded
        if hands[current_player]:
            # If the current player has their hands folded, split them into two fists
            hands[current_player] = [True, True]
        # Loop through the syllables of the rhyme
        for _ in range(syllables):
            # Increment the current player
            current_player = (current_player + 1) % len(hands)
            # Check if the current player has their hands folded
            if hands[current_player]:
                # If the current player has their hands folded, split them into two fists
                hands[current_player] = [True, True]
            # Check if the current player has already turned their hand palm down
            elif hands[current_player] == [False, False]:
                # If the current player has already turned their hand palm down, remove them from the game
                hands.pop(current_player)
                break
            # Otherwise, turn the current player's hand palm down
            else:
                hands[current_player] = [False, False]
        # Increment the current player
        current_player = (current_player + 1) % len(hands)
    # Return the number of the last player left in the game
    return len(hands)


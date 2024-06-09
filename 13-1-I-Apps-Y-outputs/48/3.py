
def coconut_splat(syllables, num_players):
    # Initialize the hands of each player as folded
    hands = [True] * num_players
    # Initialize the current player as player 1
    current_player = 0
    # Loop until only one player is left
    while len(hands) > 1:
        # If the current player has folded hands, split them into two fists
        if hands[current_player]:
            hands[current_player] = [True, True]
        # If the current player has turned their hand palm down, skip them
        elif not hands[current_player]:
            current_player = (current_player + 1) % len(hands)
            continue
        # If the current player has two fists, turn the second fist palm down
        if len(hands[current_player]) == 2:
            hands[current_player][1] = False
        # If the current player has only one fist, turn their hand palm down
        else:
            hands[current_player] = False
        # Move to the next player in clockwise order
        current_player = (current_player + 1) % len(hands)
        # If the current player has been skipped, move to the next player
        while not hands[current_player]:
            current_player = (current_player + 1) % len(hands)
    # Return the number of the last player left
    return current_player + 1


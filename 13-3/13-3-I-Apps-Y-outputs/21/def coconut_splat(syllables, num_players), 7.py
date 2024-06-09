
def coconut_splat(syllables, num_players):
    # Initialize the hands of each player as folded
    hands = [True] * num_players
    # Initialize the current player as player 1
    current_player = 0
    # Loop until only one player is left
    while len(hands) > 1:
        # Check if the current player has their hands folded
        if hands[current_player]:
            # Split the coconut into two fists
            hands[current_player] = [True, True]
        else:
            # Turn the current player's hand palm down
            hands[current_player] = False
        # Move to the next player in clockwise order
        current_player = (current_player + 1) % len(hands)
        # Check if the current player has put both hands behind their back
        if hands[current_player] == [False, False]:
            # Remove the current player from the game
            hands.pop(current_player)
    # Return the number of the last player left in the game
    return len(hands)


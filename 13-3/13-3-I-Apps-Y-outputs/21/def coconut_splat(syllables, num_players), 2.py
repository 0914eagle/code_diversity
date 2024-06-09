
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
            else:
                # If the current player has their hands turned palm down, turn the next hand palm down
                hands[current_player] = False
                current_player = (current_player + 1) % len(hands)
        # Remove any players who have turned both hands palm down
        hands = [x for x in hands if x != [False, False]]
    # Return the number of the last player left
    return len(hands) + 1



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
        else:
            # If the current player has their hands turned palm down, turn the next hand palm down
            hands[current_player] = [False] + hands[current_player]
        # Advance to the next player in clockwise order
        current_player = (current_player + 1) % len(hands)
        # If the current player has their hands turned palm down, remove them from the game
        if not hands[current_player]:
            hands.pop(current_player)
        # Advance to the next syllable in the rhyme
        syllables -= 1
        # If all syllables have been counted, start again from the first player
        if syllables == 0:
            syllables = len(hands)
    # Return the number of the player who is left
    return len(hands)


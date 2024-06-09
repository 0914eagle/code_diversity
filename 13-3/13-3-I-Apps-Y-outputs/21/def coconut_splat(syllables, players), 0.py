
def coconut_splat(syllables, players):
    # Initialize the hands of each player as folded
    hands = [True] * players
    # Initialize the current player as player 1
    current_player = 0
    # Loop through each syllable in the rhyme
    for syllable in range(syllables):
        # If the current player has folded hands, split them into two fists
        if hands[current_player]:
            hands[current_player] = [True, True]
        # If the current player has turned their hand palm down, skip them
        while not hands[current_player]:
            current_player = (current_player + 1) % players
        # If the current player has both hands behind their back, remove them from the game
        if len(hands[current_player]) == 0:
            hands[current_player] = False
            continue
        # If the current player has only one hand behind their back, remove it from the game
        if len(hands[current_player]) == 1:
            hands[current_player] = False
            continue
        # If the current player has both hands, turn the last hand palm down
        hands[current_player][-1] = False
        # Move on to the next player in clockwise order
        current_player = (current_player + 1) % players
    # Return the number of the player who is left
    return current_player + 1


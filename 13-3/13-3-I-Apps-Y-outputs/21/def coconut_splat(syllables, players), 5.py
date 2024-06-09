
def coconut_splat(syllables, players):
    # Initialize the hands of each player as folded
    hands = [True] * players
    # Initialize the current player as player 1
    current_player = 0
    # Loop through each syllable in the rhyme
    for _ in range(syllables):
        # Touch the hands of the next player clockwise
        hands[(current_player + 1) % players] = False
        # If the current player's hands are still folded, split them into two fists
        if hands[current_player]:
            hands[current_player] = [True, True]
        # If the current player's hands are already split, turn the second hand palm down
        elif isinstance(hands[current_player], list):
            hands[current_player][1] = False
        # If the current player's hands are already turned palm down, remove them from the game
        elif not hands[current_player]:
            hands[current_player] = None
        # Move on to the next player
        current_player = (current_player + 1) % players
    # Return the number of the player who is left
    return sum(1 for h in hands if h)


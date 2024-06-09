
def coconut_splat(syllables, num_players):
    # Initialize the hands of each player as folded
    hands = [True] * num_players
    # Initialize the current player as player 1
    current_player = 0
    # Loop until only one player is left
    while len(hands) > 1:
        # Check if the current player has folded hands
        if hands[current_player]:
            # If the current player has folded hands, split their hands into two fists
            hands[current_player] = [True, True]
        # Loop through the syllables of the rhyme
        for _ in range(syllables):
            # Increment the current player
            current_player = (current_player + 1) % len(hands)
            # Check if the current player has folded hands
            if hands[current_player]:
                # If the current player has folded hands, turn their hand palm down
                hands[current_player] = False
            # If the current player has a turned palm down hand, remove it from the game
            if not hands[current_player]:
                hands.remove(False)
        # If all players have turned their palms down, the game ends
        if all(not hand for hand in hands):
            break
    # Return the number of the player who is left
    return len(hands) + 1



def solve(S_A, S_B, S_C):
    # Initialize the decks
    deck_A = S_A
    deck_B = S_B
    deck_C = S_C
    
    # Initialize the current player
    current_player = "A"
    
    # While there are still cards in the decks
    while deck_A or deck_B or deck_C:
        # If the current player's deck is not empty
        if eval("deck_" + current_player):
            # Discard the top card from the current player's deck
            eval("deck_" + current_player) = eval("deck_" + current_player)[1:]
            # Determine the next player based on the letter on the discarded card
            current_player = eval("deck_" + current_player)[0]
        # If the current player's deck is empty
        else:
            # The game ends and the current player wins
            return current_player
    
    # If all decks are empty, the game ends in a draw
    return "D"


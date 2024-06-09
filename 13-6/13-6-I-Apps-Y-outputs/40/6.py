
def solve(S_A, S_B, S_C):
    # Initialize the decks of the players
    deck_A = S_A
    deck_B = S_B
    deck_C = S_C
    
    # Initialize the current player to Alice
    current_player = "A"
    
    # While there are cards in any of the decks
    while deck_A or deck_B or deck_C:
        # If the current player's deck is not empty
        if current_player == "A" and deck_A:
            # Discard the top card from Alice's deck
            deck_A = deck_A[1:]
            # Set the next player to the player whose name begins with the letter on the discarded card
            current_player = "B" if deck_B else "C"
        elif current_player == "B" and deck_B:
            deck_B = deck_B[1:]
            current_player = "C" if deck_C else "A"
        elif current_player == "C" and deck_C:
            deck_C = deck_C[1:]
            current_player = "A" if deck_A else "B"
    
    # Return the winner of the game
    return current_player


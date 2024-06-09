
def solve(S_A, S_B, S_C):
    # Initialize the decks
    deck_A = S_A
    deck_B = S_B
    deck_C = S_C
    
    # Initialize the winner
    winner = None
    
    # While all decks are not empty
    while deck_A and deck_B and deck_C:
        # Discard the top card from the current player's deck
        card = deck_A[0]
        deck_A = deck_A[1:]
        
        # Determine the next player based on the card
        if card == "a":
            next_player = deck_A
        elif card == "b":
            next_player = deck_B
        else:
            next_player = deck_C
        
        # Update the winner
        if not next_player:
            winner = "a"
            break
    
    # Return the winner
    return winner


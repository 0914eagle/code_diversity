
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    deck_a = list(s_a)
    deck_b = list(s_b)
    deck_c = list(s_c)
    
    # Initialize the winner of the game
    winner = None
    
    # While all the decks are not empty
    while deck_a and deck_b and deck_c:
        # Discard the top card from the current player's deck
        card = deck_a.pop(0)
        
        # Determine the next player based on the letter on the discarded card
        if card == "a":
            next_player = deck_a
        elif card == "b":
            next_player = deck_b
        else:
            next_player = deck_c
            
        # Add the discarded card to the next player's deck
        next_player.append(card)
        
        # If the current player's deck is empty, set the winner
        if not deck_a:
            winner = "A"
        elif not deck_b:
            winner = "B"
        elif not deck_c:
            winner = "C"
    
    # Return the winner of the game
    return winner


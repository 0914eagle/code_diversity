
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    deck_a = list(s_a)
    deck_b = list(s_b)
    deck_c = list(s_c)
    
    # Initialize the current player
    current_player = "A"
    
    # Game loop
    while True:
        # If the current player's deck is empty, the game ends and the current player wins
        if not deck_a and current_player == "A":
            return "A"
        if not deck_b and current_player == "B":
            return "B"
        if not deck_c and current_player == "C":
            return "C"
        
        # Discard the top card from the current player's deck
        if current_player == "A":
            deck_a.pop(0)
        elif current_player == "B":
            deck_b.pop(0)
        else:
            deck_c.pop(0)
        
        # Determine the next player based on the letter on the discarded card
        if current_player == "A":
            current_player = "B"
        elif current_player == "B":
            current_player = "C"
        else:
            current_player = "A"
    
    # If the game ends and no player has won, return "D"
    return "D"


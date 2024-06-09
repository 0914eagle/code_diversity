
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice_deck = list(s_a)
    bob_deck = list(s_b)
    charlie_deck = list(s_c)
    
    # Initialize the winner of the game
    winner = None
    
    # Game loop
    while alice_deck and bob_deck and charlie_deck:
        # Alice takes the first turn
        if alice_deck:
            current_player = "Alice"
            current_deck = alice_deck
        # Bob takes the second turn
        elif bob_deck:
            current_player = "Bob"
            current_deck = bob_deck
        # Charlie takes the third turn
        else:
            current_player = "Charlie"
            current_deck = charlie_deck
        
        # Discard the top card from the current player's deck
        discarded_card = current_deck.pop(0)
        
        # Determine the next player based on the letter on the discarded card
        if discarded_card == "a":
            next_player = "Alice"
        elif discarded_card == "b":
            next_player = "Bob"
        else:
            next_player = "Charlie"
        
        # Update the winner of the game
        if next_player == "Alice":
            winner = "Alice"
        elif next_player == "Bob":
            winner = "Bob"
        else:
            winner = "Charlie"
    
    # Return the winner of the game
    return winner


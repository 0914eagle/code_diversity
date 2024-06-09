
def solve(S_A, S_B, S_C):
    # Initialize the decks of the players
    decks = {
        "Alice": S_A,
        "Bob": S_B,
        "Charlie": S_C
    }
    
    # Initialize the current player
    current_player = "Alice"
    
    # While there are still cards in the decks
    while any(decks.values()):
        # Get the top card from the current player's deck
        card = decks[current_player][0]
        
        # Remove the card from the current player's deck
        decks[current_player] = decks[current_player][1:]
        
        # Determine the next player
        next_player = "Alice" if card == "a" else "Bob" if card == "b" else "Charlie"
        
        # Update the current player
        current_player = next_player
    
    # Return the winner
    return current_player


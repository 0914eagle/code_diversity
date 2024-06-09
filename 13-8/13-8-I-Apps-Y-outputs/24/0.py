
def solve(S_A, S_B, S_C):
    # Initialize the decks of the players
    decks = {
        "Alice": S_A,
        "Bob": S_B,
        "Charlie": S_C
    }
    
    # Initialize the current player and the order of the players
    current_player = "Alice"
    player_order = ["Alice", "Bob", "Charlie"]
    
    # While there are still cards in the decks
    while any(decks.values()):
        # Get the current player's deck
        current_deck = decks[current_player]
        
        # If the current player's deck is not empty
        if current_deck:
            # Discard the top card from the current player's deck
            current_deck = current_deck[1:]
            
            # Get the next player's name based on the letter on the discarded card
            next_player = player_order[(player_order.index(current_player) + 1) % len(player_order)]
            
            # Update the current player and the decks
            current_player = next_player
            decks[current_player] = current_deck
        else:
            # If the current player's deck is empty, the game ends and the current player wins
            return current_player
    
    # If all the decks are empty, the game ends and no player wins
    return "None"


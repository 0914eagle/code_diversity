
def determine_winner(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice_deck = [c for c in s_a]
    bob_deck = [c for c in s_b]
    charlie_deck = [c for c in s_c]
    
    # While all decks are not empty
    while alice_deck and bob_deck and charlie_deck:
        # Alice goes first
        current_player = 0
        
        # While the current player's deck is not empty
        while alice_deck and current_player == 0:
            # Discard the top card in the current player's deck
            card = alice_deck.pop(0)
            
            # Determine the next player based on the letter on the card
            if card == "a":
                current_player = 0
            elif card == "b":
                current_player = 1
            else:
                current_player = 2
        
        # If the current player's deck is empty, they win the game
        if not alice_deck:
            return "A"
        
        # Swap the current player with the next player
        current_player = (current_player + 1) % 3
    
    # If Alice's deck is empty, Bob wins the game
    if not bob_deck:
        return "B"
    
    # If Bob's deck is empty, Charlie wins the game
    if not charlie_deck:
        return "C"
    
    # If all decks are not empty, the game continues
    return "D"



def determine_winner(S_A, S_B, S_C):
    # Initialize variables
    deck_A = S_A
    deck_B = S_B
    deck_C = S_C
    winner = None

    # While all decks have at least one card, continue playing the game
    while len(deck_A) > 0 and len(deck_B) > 0 and len(deck_C) > 0:
        # Discard top card from current player's deck
        current_player = deck_A[0]
        deck_A = deck_A[1:]

        # Determine next player based on card value
        if current_player == "a":
            next_player = deck_A
        elif current_player == "b":
            next_player = deck_B
        else:
            next_player = deck_C

        # Update current player's deck
        current_player_deck = next_player

        # Update winner if a player's deck is empty
        if len(current_player_deck) == 0:
            winner = current_player
            break

    # Return winner
    return winner


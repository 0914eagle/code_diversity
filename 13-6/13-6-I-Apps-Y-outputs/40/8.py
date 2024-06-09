
def find_winner(S_A, S_B, S_C):
    # Initialize the winner as None
    winner = None

    # Create a dictionary to map the letters to the players
    letter_to_player = {"a": "Alice", "b": "Bob", "c": "Charlie"}

    # Create a dictionary to store the decks of each player
    decks = {"Alice": S_A, "Bob": S_B, "Charlie": S_C}

    # Loop until a player's deck is empty
    while any(decks.values()):
        # Find the current player by checking the top letter of their deck
        current_player = letter_to_player[decks["Alice"][0]]

        # Discard the top card from the current player's deck
        decks[current_player] = decks[current_player][1:]

        # If the current player's deck is empty, set the winner
        if not decks[current_player]:
            winner = current_player
            break

    # Return the winner
    return winner


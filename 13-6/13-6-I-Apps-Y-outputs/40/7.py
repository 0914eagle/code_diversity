
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice_deck = [c for c in s_a]
    bob_deck = [c for c in s_b]
    charlie_deck = [c for c in s_c]

    # Initialize the current player
    current_player = "A"

    # While there are still cards in the decks
    while alice_deck or bob_deck or charlie_deck:
        # If the current player's deck is not empty
        if current_player == "A" and alice_deck:
            current_player = alice_deck.pop()
        elif current_player == "B" and bob_deck:
            current_player = bob_deck.pop()
        elif current_player == "C" and charlie_deck:
            current_player = charlie_deck.pop()
        else:
            break

    # Return the winner
    if current_player == "A":
        return "A"
    elif current_player == "B":
        return "B"
    else:
        return "C"


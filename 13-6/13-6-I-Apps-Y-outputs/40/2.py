
def solve(s_a, s_b, s_c):
    # Initialize the decks of the players
    alice_deck = [c for c in s_a]
    bob_deck = [c for c in s_b]
    charlie_deck = [c for c in s_c]

    # Game loop
    while alice_deck and bob_deck and charlie_deck:
        # Alice's turn
        if alice_deck:
            card = alice_deck.pop(0)
            if card == "a":
                next_player = "b"
            elif card == "b":
                next_player = "c"
            else:
                next_player = "a"
        # Bob's turn
        elif bob_deck:
            card = bob_deck.pop(0)
            if card == "a":
                next_player = "c"
            elif card == "b":
                next_player = "a"
            else:
                next_player = "b"
        # Charlie's turn
        else:
            card = charlie_deck.pop(0)
            if card == "a":
                next_player = "b"
            elif card == "b":
                next_player = "c"
            else:
                next_player = "a"

        # Update the deck of the next player
        if next_player == "a":
            alice_deck.append(card)
        elif next_player == "b":
            bob_deck.append(card)
        else:
            charlie_deck.append(card)

    # Determine the winner
    if alice_deck:
        return "A"
    elif bob_deck:
        return "B"
    else:
        return "C"


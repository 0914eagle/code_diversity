
def one_card_poker(alice_card, bob_card):
    alice_card = int(alice_card)
    bob_card = int(bob_card)
    if alice_card > bob_card:
        return "Alice"
    elif bob_card > alice_card:
        return "Bob"
    else:
        return "Draw"


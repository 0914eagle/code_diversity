
def one_card_poker(a, b):
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    alice_value = card_values.index(a) + 1
    bob_value = card_values.index(b) + 1
    if alice_value > bob_value:
        return "Alice"
    elif alice_value < bob_value:
        return "Bob"
    else:
        return "Draw"


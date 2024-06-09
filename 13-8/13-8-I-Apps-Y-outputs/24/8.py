
def find_winner(s_a, s_b, s_c):
    deck_a = list(s_a)
    deck_b = list(s_b)
    deck_c = list(s_c)
    while deck_a and deck_b and deck_c:
        card_a = deck_a.pop(0)
        if card_a == "a":
            break
        elif card_a == "b":
            deck_b.pop(0)
        else:
            deck_c.pop(0)
        if not deck_a:
            break
        card_b = deck_b.pop(0)
        if card_b == "b":
            break
        elif card_b == "c":
            deck_c.pop(0)
        else:
            deck_a.pop(0)
        if not deck_b:
            break
        card_c = deck_c.pop(0)
        if card_c == "c":
            break
        elif card_c == "a":
            deck_a.pop(0)
        else:
            deck_b.pop(0)
    if deck_a:
        return "A"
    elif deck_b:
        return "B"
    else:
        return "C"


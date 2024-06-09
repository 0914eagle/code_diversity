
def solve(S_A, S_B, S_C):
    deck_A = list(S_A)
    deck_B = list(S_B)
    deck_C = list(S_C)
    while deck_A and deck_B and deck_C:
        card_A = deck_A.pop(0)
        if card_A == "a":
            turn = "A"
        elif card_A == "b":
            turn = "B"
        else:
            turn = "C"
        if turn == "A":
            deck_A.extend(deck_B.pop(0))
        elif turn == "B":
            deck_B.extend(deck_C.pop(0))
        else:
            deck_C.extend(deck_A.pop(0))
    if deck_A:
        return "A"
    elif deck_B:
        return "B"
    else:
        return "C"


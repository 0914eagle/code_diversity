
def get_max_score(a, b):
    score = 0
    deck = []
    while a > 0 or b > 0:
        if a > 0:
            deck.append("o")
            a -= 1
        if b > 0:
            deck.append("x")
            b -= 1
    for i in range(len(deck) - 1):
        if deck[i] == deck[i + 1] and deck[i] == "o":
            score += (i + 1) ** 2
        elif deck[i] == deck[i + 1] and deck[i] == "x":
            score -= (i + 1) ** 2
    return score, "".join(deck)



def shuffle_deck(deck):
    n = len(deck)
    shuffles = 0
    while deck != list(range(1, n+1)):
        deck = [deck[i] for i in range(0, n, 2)] + [deck[i] for i in range(1, n, 2)]
        shuffles += 1
    return shuffles


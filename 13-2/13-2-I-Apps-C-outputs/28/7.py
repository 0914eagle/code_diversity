
def shuffle_deck(deck):
    n = len(deck)
    shuffles = 0
    while deck != list(range(1, n+1)):
        deck = [deck[i-1] if i % 2 == 0 else deck[n-i] for i in range(n)]
        shuffles += 1
    return shuffles


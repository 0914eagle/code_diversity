
def solve(deck):
    # Sort the deck in descending order
    deck.sort(reverse=True)
    # Initialize the maximum number of remaining cards
    max_cards = 0
    # Loop through the deck and find the maximum number of remaining cards
    for i in range(len(deck)):
        # If the current card is not the largest card, eat the largest card and the current card
        if deck[i] != deck[0]:
            max_cards += 2
        # If the current card is the largest card, eat the largest card and the smallest card
        else:
            max_cards += 1
    return max_cards


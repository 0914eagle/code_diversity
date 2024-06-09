
def solve(deck):
    # Sort the deck in descending order
    deck.sort(reverse=True)
    # Initialize the maximum number of remaining cards
    max_cards = 0
    # Loop through the deck and find the maximum number of remaining cards
    for i in range(len(deck)):
        # If the current card is not the largest card, eat it
        if deck[i] != deck[0]:
            deck.pop(i)
        # Update the maximum number of remaining cards
        max_cards = max(max_cards, len(deck))
    # Return the maximum number of remaining cards
    return max_cards


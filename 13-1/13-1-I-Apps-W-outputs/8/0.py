
def get_max_remaining_cards(deck):
    
    # Sort the deck in non-decreasing order
    deck.sort()
    # Initialize the maximum number of remaining cards to the length of the deck
    max_remaining_cards = len(deck)
    # Loop through the deck and find the largest and smallest values
    for i in range(len(deck)):
        if i + 2 < len(deck):
            # If the current value is the largest value, eat the next two values and return the remaining value to the deck
            if deck[i] == deck[0]:
                max_remaining_cards = max(max_remaining_cards, len(deck) - 3)
            # If the current value is the smallest value, eat the previous two values and return the remaining value to the deck
            elif deck[i] == deck[-1]:
                max_remaining_cards = max(max_remaining_cards, len(deck) - 3)
    return max_remaining_cards


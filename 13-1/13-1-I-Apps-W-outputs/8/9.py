
def get_max_remaining_cards(deck):
    
    # Sort the deck in non-decreasing order
    deck.sort()
    # Initialize the maximum number of remaining cards to the length of the deck
    max_remaining_cards = len(deck)
    # Loop through the deck and find the largest and smallest values
    for i in range(len(deck)):
        if i + 2 < len(deck):
            # If the current value is larger than the next two values, eat the next two values and return the current value
            if deck[i] > deck[i + 1] and deck[i] > deck[i + 2]:
                max_remaining_cards -= 2
                i += 2
            # If the current value is smaller than the next two values, eat the current value and return the next two values
            elif deck[i] < deck[i + 1] and deck[i] < deck[i + 2]:
                max_remaining_cards -= 1
                i += 2
    return max_remaining_cards

if __name__ == '__main__':
    deck = [int(x) for x in input().split()]
    print(get_max_remaining_cards(deck))


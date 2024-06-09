
def get_max_remaining_cards(deck):
    
    # Sort the deck in descending order
    deck.sort(reverse=True)
    # Initialize the maximum number of remaining cards to the length of the deck
    max_remaining_cards = len(deck)
    # Loop through the deck and find the largest and smallest values
    for i in range(len(deck)):
        largest = deck[0]
        smallest = deck[-1]
        # If the largest and smallest values are not the same, break the loop
        if largest != smallest:
            break
    # If the largest and smallest values are the same, return the maximum number of remaining cards
    if largest == smallest:
        return max_remaining_cards
    # Loop through the deck and find the indices of the largest and smallest values
    for i in range(len(deck)):
        if deck[i] == largest:
            largest_index = i
        if deck[i] == smallest:
            smallest_index = i
    # Eat the two cards with the largest and smallest values and return the remaining card to the deck
    deck[largest_index] = 0
    deck[smallest_index] = 0
    # Remove the eaten cards from the deck
    deck = [x for x in deck if x != 0]
    # Return the maximum number of remaining cards
    return len(deck)

if __name__ == '__main__':
    deck = [1, 2, 1, 3, 7]
    print(get_max_remaining_cards(deck))


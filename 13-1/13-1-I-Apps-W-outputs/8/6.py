
def get_max_remaining_cards(deck):
    
    # Sort the deck in non-decreasing order
    deck.sort()
    # Initialize the maximum number of remaining cards to the length of the deck
    max_remaining_cards = len(deck)
    # Loop through the deck and find the largest and smallest values
    for i in range(len(deck)):
        largest = deck[0]
        smallest = deck[-1]
        # If the largest and smallest values are not the same, break the loop
        if largest != smallest:
            break
    # Loop through the deck and find the second largest and second smallest values
    for i in range(1, len(deck)):
        if deck[i] > largest:
            second_largest = largest
            largest = deck[i]
        elif deck[i] < smallest:
            second_smallest = smallest
            smallest = deck[i]
    # Find the number of remaining cards by subtracting the number of cards eaten from the length of the deck
    num_remaining_cards = len(deck) - 2
    # If the number of remaining cards is greater than the maximum number of remaining cards, update the maximum number of remaining cards
    if num_remaining_cards > max_remaining_cards:
        max_remaining_cards = num_remaining_cards
    # Return the maximum number of remaining cards
    return max_remaining_cards

def main():
    # Read the input deck from stdin
    deck = list(map(int, input().split()))
    # Find the maximum number of remaining cards
    max_remaining_cards = get_max_remaining_cards(deck)
    # Print the maximum number of remaining cards
    print(max_remaining_cards)

if __name__ == '__main__':
    main()


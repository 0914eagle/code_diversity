
def solve(n, a, b):
    # Initialize the variables
    operations = 0
    cards_in_hand = a
    cards_in_pile = b

    # Sort the cards in the pile in increasing order
    cards_in_pile.sort()

    # Loop through the cards in the pile and play the cards in the hand
    for i in range(n):
        # If the card in the hand is not empty, play it and draw the top card from the pile
        if cards_in_hand[i] != 0:
            operations += 1
            cards_in_hand[i] = 0
            cards_in_pile.append(cards_in_pile.pop(0))

    # Return the minimum number of operations
    return operations


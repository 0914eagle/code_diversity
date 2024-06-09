
def solve(n, a, b):
    # Initialize the variables
    operations = 0
    cards_in_hand = a
    cards_in_pile = b
    cards_piled_up = [0] * n

    # Loop through the cards in hand and pile
    for i in range(n):
        # If the card is not empty, play it and draw the top card from the pile
        if cards_in_hand[i] != 0:
            operations += 1
            cards_in_hand[i] = 0
            cards_piled_up[i] = cards_in_pile[0]
            cards_in_pile = cards_in_pile[1:]

        # If the card is empty, draw the top card from the pile
        else:
            operations += 1
            cards_in_hand[i] = cards_in_pile[0]
            cards_in_pile = cards_in_pile[1:]

    # Return the minimum number of operations
    return operations


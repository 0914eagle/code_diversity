
def arithmetic_progression(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the difference between consecutive cards
    diff = 0

    # Iterate through the cards and calculate the difference
    for i in range(n - 1):
        diff = cards[i + 1] - cards[i]

    # If the difference is equal to 1, return -1
    if diff == 1:
        return -1

    # Initialize a list to store the integers that can be written on the card
    integers = []

    # Iterate through the cards and calculate the integers that can be written on the card
    for i in range(n):
        integers.append(cards[i] + (i + 1) * diff)

    # Return the list of integers
    return integers


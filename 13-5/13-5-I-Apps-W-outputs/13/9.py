
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the number of integers that can be written on the card
    num_ints = 0

    # Check if the cards form an arithmetic progression
    if n == 1:
        return [-1]
    elif n == 2:
        if cards[1] - cards[0] == 1:
            return [-1]
        else:
            return [cards[1] - cards[0] - 1]
    else:
        # Calculate the difference between consecutive cards
        diff = cards[1] - cards[0]
        for i in range(2, n):
            if cards[i] - cards[i - 1] != diff:
                break
        else:
            # All cards form an arithmetic progression, so there is only one integer that can be written on the card
            return [-1]

        # Calculate the number of integers that can be written on the card
        num_ints = (cards[n - 1] - cards[0]) // diff

        # Return the numbers in increasing order
        return list(range(cards[0], cards[0] + num_ints * diff, diff))


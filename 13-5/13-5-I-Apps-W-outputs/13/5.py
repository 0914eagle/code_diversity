
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the number of integers that can be written on the card
    num_integers = 0

    # Initialize the list of integers that can be written on the card
    integers = []

    # Check if the cards form an arithmetic progression
    if n == 1:
        # If there is only one card, we can write any integer on it
        num_integers = -1
    elif n == 2:
        # If there are two cards, we can write any two distinct integers on them
        num_integers = -1
    else:
        # If there are three or more cards, we need to check if the difference between the first two cards is equal to the difference between the second and third cards, and so on
        for i in range(1, n):
            if cards[i] - cards[i-1] != cards[1] - cards[0]:
                # If the differences are not equal, we cannot form an arithmetic progression
                break
        else:
            # If the differences are equal for all pairs of consecutive cards, we can form an arithmetic progression
            num_integers = 1
            integers.append(cards[1] - cards[0])

    return num_integers, integers


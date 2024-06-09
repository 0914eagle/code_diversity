
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the result
    result = []

    # Check if the cards can form an arithmetic progression
    if n == 1:
        return [-1]
    if n == 2:
        if cards[1] - cards[0] == 1:
            return [-1]
        else:
            return [cards[1] - cards[0] - 1]

    # Check if the cards can form an arithmetic progression with a common difference of 1
    if all(cards[i+1] - cards[i] == 1 for i in range(n-1)):
        return [-1]

    # Check if the cards can form an arithmetic progression with a common difference of 2
    if all(cards[i+1] - cards[i] == 2 for i in range(n-1)):
        return [1]

    # Check if the cards can form an arithmetic progression with a common difference of k
    for k in range(2, n):
        if all(cards[i+1] - cards[i] == k for i in range(n-1)):
            return [k]

    # If no common difference can form an arithmetic progression, return 0
    return [0]


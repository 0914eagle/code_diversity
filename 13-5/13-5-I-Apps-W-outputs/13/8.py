
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()

    # Initialize the result list
    result = []

    # Check if the cards can form an arithmetic progression
    if n == 1:
        return [-1]
    if n == 2:
        if cards[1] - cards[0] == 1:
            return [-1]
        else:
            return [cards[1] - cards[0] - 1]

    # Calculate the common difference of the arithmetic progression
    common_diff = cards[1] - cards[0]
    for i in range(2, n):
        if cards[i] - cards[i - 1] != common_diff:
            return [-1]

    # Calculate the first term of the arithmetic progression
    first_term = cards[0]

    # Calculate the last term of the arithmetic progression
    last_term = cards[n - 1] + common_diff

    # Generate all possible values of the additional card
    for i in range(first_term, last_term + 1):
        if i not in cards:
            result.append(i)

    return result



def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()
    
    # Initialize a set to store the possible values of the extra card
    values = set()
    
    # Iterate over the cards and calculate the difference between each two consecutive cards
    for i in range(n - 1):
        diff = cards[i + 1] - cards[i]
        values.add(diff)
    
    # If the set of possible values has only one element, it means that the cards can be arranged in an arithmetic progression
    if len(values) == 1:
        return -1
    else:
        # Return the set of possible values as the answer
        return len(values), sorted(list(values))


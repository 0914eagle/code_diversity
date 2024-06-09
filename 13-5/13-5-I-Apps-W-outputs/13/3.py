
def solve(n, cards):
    # Sort the cards in increasing order
    cards.sort()
    
    # Initialize a set to store the possible values of the additional card
    values = set()
    
    # Iterate over the cards and calculate the difference between consecutive cards
    for i in range(n - 1):
        diff = cards[i + 1] - cards[i]
        values.add(diff)
    
    # If the set of values has only one element, then it is impossible to find an additional card with a suitable value
    if len(values) == 1:
        return -1
    
    # If the set of values has more than one element, then return the set of values
    return list(values)


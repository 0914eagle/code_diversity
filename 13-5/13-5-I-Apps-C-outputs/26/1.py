
def solve(x, y):
    # Check if x and y are valid inputs
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"
    
    # Initialize variables
    oranges = x
    apples = y
    cards = []
    
    # Loop until all fruits are consumed
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A' or 'B'
        if oranges > apples:
            cards.append("A")
            oranges -= 1
        else:
            cards.append("B")
            apples -= 1
    
    # Return the sequence of cards
    return "".join(cards)



def solve(x, y):
    # Check if x and y are valid inputs
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"
    
    # Initialize variables
    oranges = x
    apples = y
    cards = []
    
    # Loop until all fruits are gone
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A' or 'B'
        if oranges > apples:
            cards.append("A")
            oranges -= 1
        else:
            cards.append("B")
            apples -= 1
    
    # Compress the sequence of cards
    compressed_cards = ""
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards += str(count) + cards[i]
            count = 1
    compressed_cards += str(count) + cards[-1]
    
    return compressed_cards


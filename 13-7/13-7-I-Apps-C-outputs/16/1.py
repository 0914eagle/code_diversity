
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
        # Check if there are more oranges than apples
        if oranges > apples:
            # Add card with letter 'A'
            cards.append("A")
            # Give all oranges to Bob
            oranges, apples = apples, oranges
        # Check if there are more apples than oranges
        elif apples > oranges:
            # Add card with letter 'B'
            cards.append("B")
            # Give all apples to Alice
            oranges, apples = oranges, apples
        # Check if there are an equal number of oranges and apples
        else:
            # Add card with letter 'A'
            cards.append("A")
            # Give all oranges to Bob
            oranges, apples = apples, oranges
    
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


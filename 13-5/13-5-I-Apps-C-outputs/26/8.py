
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
        # Add a card with letter 'A'
        cards.append("A")
        oranges -= 1
        
        # Add a card with letter 'B'
        cards.append("B")
        apples -= 1
    
    # Check if there are any remaining fruits
    if oranges > 0 or apples > 0:
        return "Impossible"
    
    # Compress the sequence of cards
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count) + cards[i])
            count = 1
    compressed_cards.append(str(count) + cards[-1])
    
    return "".join(compressed_cards)


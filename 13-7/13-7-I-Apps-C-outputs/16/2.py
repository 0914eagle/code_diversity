
def solve(x, y):
    # Check if x and y are valid inputs
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"
    
    # Initialize variables
    oranges = x
    apples = y
    cards = []
    
    # Play the game
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A'
        cards.append("A")
        oranges -= 1
        apples -= 1
        
        # Add a card with letter 'B'
        cards.append("B")
        oranges += 1
        apples += 1
    
    # Compress the sequence of cards
    compressed_cards = ""
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards += str(count) + cards[i]
            count = 1
    
    # Add the last card
    compressed_cards += str(count) + cards[-1]
    
    return compressed_cards


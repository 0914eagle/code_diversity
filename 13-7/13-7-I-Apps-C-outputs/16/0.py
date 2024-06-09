
def solve(x, y):
    # Check if x and y are valid inputs
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"
    
    # Initialize variables
    oranges = x
    apples = y
    cards = []
    
    # Game loop
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A'
        cards.append("A")
        oranges -= 1
        apples -= 1
        
        # Add a card with letter 'B'
        cards.append("B")
        oranges += 1
        apples += 1
    
    # Return the compressed string of cards
    return "".join(cards)


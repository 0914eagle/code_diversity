
def solve(x, y):
    # Check if x and y are positive
    if x <= 0 or y <= 0:
        return "Impossible"
    
    # Initialize variables
    oranges = x
    apples = y
    cards = []
    
    # While there are still oranges and apples left
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A'
        cards.append("A")
        oranges -= 1
        apples -= 1
    
    # If there are still oranges left, add cards with letter 'B'
    while oranges > 0:
        cards.append("B")
        oranges -= 1
    
    # If there are still apples left, add cards with letter 'A'
    while apples > 0:
        cards.append("A")
        apples -= 1
    
    # Return the compressed string of cards
    return "".join(cards)


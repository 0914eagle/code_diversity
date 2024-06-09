
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
        # Add card to the sequence
        cards.append("A")
        oranges -= 1
        apples -= 1
        
        # Check if the game is over
        if oranges == 0 or apples == 0:
            break
        
        # Add card to the sequence
        cards.append("B")
        oranges -= 1
        apples -= 1
    
    # Check if the game is over
    if oranges == 0 and apples == 0:
        return "".join(cards)
    
    # If the game is not over, return Impossible
    return "Impossible"


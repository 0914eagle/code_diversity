
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
        # Add card to the sequence
        cards.append("A")
        oranges -= 1
        apples -= 1
    
    # Check if there are any remaining fruits
    if oranges > 0 or apples > 0:
        return "Impossible"
    
    # Compress the sequence of cards
    compressed_cards = []
    count = 1
    for i in range(len(cards)):
        if i == 0:
            compressed_cards.append(cards[i])
        elif cards[i] == cards[i-1]:
            count += 1
        else:
            compressed_cards.append(str(count))
            compressed_cards.append(cards[i])
            count = 1
    
    # Return the compressed sequence of cards
    return "".join(compressed_cards)


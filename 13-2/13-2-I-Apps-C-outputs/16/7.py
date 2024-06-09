
def get_cards(x, y):
    # Initialize variables
    oranges = x
    apples = y
    cards = []

    # Check if the number of oranges and apples is valid
    if x < 1 or y < 1 or x * y < 2:
        return "Impossible"

    # Add cards to the list
    while oranges > 0 and apples > 0:
        # Add a card with letter 'A' if there are oranges left
        if oranges > 0:
            cards.append("A")
            oranges -= 1
        # Add a card with letter 'B' if there are apples left
        if apples > 0:
            cards.append("B")
            apples -= 1

    # Compress the cards list
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count) + cards[i])
            count = 1
    compressed_cards.append(str(count) + cards[-1])

    # Return the compressed cards list
    return "".join(compressed_cards)


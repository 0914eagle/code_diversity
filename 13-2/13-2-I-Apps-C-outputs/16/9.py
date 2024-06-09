
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
        # Add a card with letter 'A' if there are more oranges than apples
        if oranges > apples:
            cards.append("A")
            oranges -= 1
        # Add a card with letter 'B' if there are more apples than oranges
        elif apples > oranges:
            cards.append("B")
            apples -= 1
        # If the number of oranges and apples is equal, add a card with letter 'A'
        else:
            cards.append("A")
            oranges -= 1

    # Return the compressed string of cards
    return "".join(cards)



def get_cards(x, y):
    # Initialize variables
    oranges = x
    apples = y
    cards = []

    # Loop until all fruits are gone
    while oranges > 0 and apples > 0:
        # Check if there are more oranges than apples
        if oranges > apples:
            # Add card with letter 'A'
            cards.append('A')
            # Give all oranges to Bob
            oranges -= apples
        # Check if there are more apples than oranges
        elif apples > oranges:
            # Add card with letter 'B'
            cards.append('B')
            # Give all apples to Alice
            apples -= oranges
        # Check if there are equal number of oranges and apples
        else:
            # Add card with letter 'A'
            cards.append('A')
            # Give all oranges to Bob
            oranges -= apples
            # Add card with letter 'B'
            cards.append('B')
            # Give all apples to Alice
            apples -= oranges

    # Return compressed string of cards
    return ''.join([str(len(list(group))) + char for char, group in groupby(cards)])


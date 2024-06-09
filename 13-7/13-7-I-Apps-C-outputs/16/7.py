
def solve(x, y):
    # Initialize variables
    oranges = x
    apples = y
    cards = []

    # Loop until all fruits are gone
    while oranges > 0 and apples > 0:
        # Add card with letter 'A'
        cards.append('A')
        oranges -= 1
        apples -= 1

        # Add card with letter 'B'
        cards.append('B')
        oranges += 1
        apples += 1

    # Check if there are any remaining fruits
    if oranges == 0 and apples == 0:
        return "".join(cards)
    else:
        return "Impossible"


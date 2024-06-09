
def solve(deck):
    # Step 1: Sort the deck in descending order
    deck.sort(reverse=True)

    # Step 2: Eat the two cards with the largest and smallest values
    deck.pop()
    deck.pop(0)

    # Step 3: Return the remaining card to the deck
    deck.append(deck.pop(0))

    # Step 4: Return the length of the deck
    return len(deck)


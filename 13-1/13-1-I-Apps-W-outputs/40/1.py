
def solve(deck):
    # Step 1: Sort the deck in descending order
    deck.sort(reverse=True)

    # Step 2: Eat the largest and smallest values
    largest = deck.pop()
    smallest = deck.pop()

    # Step 3: Return the remaining card to the deck
    deck.append(largest)

    # Step 4: Return the number of remaining cards
    return len(deck)


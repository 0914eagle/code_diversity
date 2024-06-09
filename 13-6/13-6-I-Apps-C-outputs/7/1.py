
def solve(n, a):
    # Initialize the answer and the pile
    answer = 0
    pile = []

    # Loop through each box
    for i in range(n):
        # If the current box is not available, skip it
        if a[i] == 0:
            continue

        # If the current box is available, add it to the pile
        pile.append(a[i])

        # If the current box is a multiple of any other box in the pile, remove it from the pile
        for j in range(len(pile)):
            if a[i] % pile[j] == 0:
                pile.remove(pile[j])
                break

    # Return the number of distinct piles
    return len(pile)


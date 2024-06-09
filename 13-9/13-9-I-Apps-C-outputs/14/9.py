
def get_possible_two_suspect_sets(n, p, names):
    # Initialize a set to store the possible two-suspect sets
    possible_sets = set()

    # Iterate over the names of the coders
    for i in range(n):
        # Get the names of the coders named by the current coder
        x, y = names[i]

        # If both coders named by the current coder are in the possible sets, add them to the current set
        if x in possible_sets and y in possible_sets:
            possible_sets.add((i, x))
            possible_sets.add((i, y))

    # Return the number of possible two-suspect sets
    return len(possible_sets)


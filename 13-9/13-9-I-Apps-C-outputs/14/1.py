
def count_two_suspects(n, p, names):
    # Initialize a dictionary to store the number of coders named by each coder
    named_by = {}
    for i in range(n):
        named_by[i + 1] = set()

    # Populate the dictionary with the names of the coders named by each coder
    for i, name in enumerate(names):
        named_by[i + 1].update(name)

    # Initialize a set to store the two suspects
    suspects = set()

    # Iterate over the dictionary and count the number of coders who named at least one of the two suspects
    count = 0
    for i in range(n):
        if len(suspects) < 2:
            suspects.add(i + 1)
        if len(suspects) == 2:
            count += len(named_by[i + 1].intersection(suspects))

    return count


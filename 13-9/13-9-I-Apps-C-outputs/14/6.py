
import itertools

def get_number_of_suspect_sets(n, p, names):
    # Initialize a set to store the names of the coders who agreed with the head's choice
    agreed_coders = set()

    # Iterate over the names of the coders
    for name in names:
        # If the coder named at least one of the two suspects, add their name to the set of agreed coders
        if name[0] in agreed_coders or name[1] in agreed_coders:
            agreed_coders.add(name[0])
            agreed_coders.add(name[1])

    # Return the number of two-suspect sets that have at least p coders who agreed with the head's choice
    return len([s for s in itertools.combinations(range(1, n + 1), 2) if len(agreed_coders.intersection(s)) >= p])


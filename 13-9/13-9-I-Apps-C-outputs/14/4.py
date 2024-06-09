
def get_number_of_possible_suspects(n, p, coders):
    # Initialize a set to store the suspected coders
    suspected_coders = set()

    # Iterate over the coders and add their suspected coders to the set
    for coder in coders:
        suspected_coders.update(coder)

    # Get the number of unique suspected coders
    num_unique_suspected_coders = len(suspected_coders)

    # Calculate the number of possible two-suspect sets
    num_possible_suspects = num_unique_suspected_coders * (num_unique_suspected_coders - 1) // 2

    # Return the number of possible two-suspect sets
    return num_possible_suspects


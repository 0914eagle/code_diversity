
def solve(n, live_sequence, fossil_sequences):
    # Initialize variables
    first_path = []
    second_path = []
    impossible = False

    # Add the live sequence to the first path
    first_path.append(live_sequence)

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is already in the first path
        if sequence in first_path:
            # If it is, add it to the second path
            second_path.append(sequence)
        # If it's not in the first path, add it to the first path
        else:
            first_path.append(sequence)

    # Check if it's possible to have two evolutionary paths
    if len(first_path) + len(second_path) == len(fossil_sequences):
        # If it is, return the two paths
        return len(first_path), len(second_path), first_path, second_path
    # If it's not, return the word impossible
    else:
        return "impossible"



def restore_sequence(n, l_r_pairs):
    # Initialize an empty sequence
    sequence = []

    # Iterate through the l_r_pairs
    for l, r in l_r_pairs:
        # Check if the sequence is empty
        if not sequence:
            # Add the first opening bracket
            sequence.append("(")

        # Check if the last element of the sequence is an opening bracket
        if sequence[-1] == "(":
            # Add the corresponding closing bracket
            sequence.append(")")
        else:
            # Add an opening bracket
            sequence.append("(")

    # Check if the sequence is complete
    if len(sequence) != 2 * n:
        return "IMPOSSIBLE"

    # Return the sequence
    return "".join(sequence)


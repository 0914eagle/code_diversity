
def solve(n, current_sequence, fossil_sequences):
    # Initialize variables
    first_path = []
    second_path = []
    impossible = False

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is in the current sequence
        if sequence in current_sequence:
            # Add the sequence to the first path
            first_path.append(sequence)
        else:
            # Add the sequence to the second path
            second_path.append(sequence)

    # Check if both paths have at least one sequence
    if len(first_path) == 0 or len(second_path) == 0:
        impossible = True

    # Return the results
    if impossible:
        return "impossible"
    else:
        return str(len(first_path)) + " " + str(len(second_path)) + "\n" + "\n".join(first_path) + "\n" + "\n".join(second_path)



def restore_sequence(n, l_list, r_list):
    # Initialize an empty sequence
    sequence = []

    # Iterate through the list of opening brackets
    for i in range(n):
        # Find the corresponding closing bracket for the current opening bracket
        closing_bracket = sequence[l_list[i] - 1] if l_list[i] > 0 else sequence[r_list[i] - 1]

        # Check if the closing bracket is already present in the sequence
        if closing_bracket in sequence:
            # If the closing bracket is already present, it means that we have a mismatch
            return "IMPOSSIBLE"
        else:
            # If the closing bracket is not present, add it to the sequence
            sequence.append(closing_bracket)

    # If we reach this point, it means that we have successfully restored the sequence
    return "".join(sequence)


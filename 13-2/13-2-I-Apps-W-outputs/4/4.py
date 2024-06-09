
def restore_sequence(n, l_list, r_list):
    # Initialize an empty sequence
    sequence = []

    # Iterate through the list of opening brackets
    for i in range(n):
        # Find the corresponding closing bracket for the current opening bracket
        closing_bracket = sequence[l_list[i] - 1] if l_list[i] > 0 else sequence[r_list[i] - 1]

        # Check if the distance between the opening and closing brackets is within the allowed range
        if abs(l_list[i] - r_list[i]) <= r_list[i]:
            # Add the opening and closing brackets to the sequence
            sequence.append("(")
            sequence.append(")")
        else:
            # If the distance is not within the allowed range, return "IMPOSSIBLE"
            return "IMPOSSIBLE"

    # If all the brackets are added successfully, return the sequence
    return "".join(sequence)


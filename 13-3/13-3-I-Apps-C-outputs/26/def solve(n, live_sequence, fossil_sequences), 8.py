
def solve(n, live_sequence, fossil_sequences):
    # Initialize variables
    first_path = []
    second_path = []
    impossible = False

    # Add the live sequence to the first path
    first_path.append(live_sequence)

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # If the sequence is not in the first path, add it to the second path
        if sequence not in first_path:
            second_path.append(sequence)
        # If the sequence is already in the first path, it cannot be in the second path as well
        else:
            impossible = True
            break

    # If impossible is True, return the word impossible
    if impossible:
        return "impossible"
    # Otherwise, return the number of sequences in the first and second paths, followed by the sequences in each path
    else:
        return str(len(first_path)) + " " + str(len(second_path)) + "\n" + "\n".join(first_path) + "\n" + "\n".join(second_path)


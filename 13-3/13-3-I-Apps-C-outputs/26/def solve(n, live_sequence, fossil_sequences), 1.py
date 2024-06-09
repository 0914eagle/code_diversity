
def solve(n, live_sequence, fossil_sequences):
    # Initialize a dictionary to store the fossil sequences and their corresponding evolutionary paths
    paths = {}

    # Iterate through the fossil sequences and assign them to the corresponding evolutionary path
    for sequence in fossil_sequences:
        # If the sequence is not in the dictionary, add it to the dictionary with a new evolutionary path
        if sequence not in paths:
            paths[sequence] = len(paths) + 1
        # If the sequence is already in the dictionary, add it to the existing evolutionary path
        else:
            paths[sequence] = paths[sequence]

    # Initialize variables to store the number of sequences in the first and second evolutionary paths
    s1 = 0
    s2 = 0

    # Iterate through the fossil sequences and count the number of sequences in the first and second evolutionary paths
    for sequence in fossil_sequences:
        if paths[sequence] == 1:
            s1 += 1
        elif paths[sequence] == 2:
            s2 += 1

    # If it is possible to find two evolutionary paths in the fossil record, return the sequences in the two paths
    if s1 > 0 and s2 > 0:
        return [s1, s2] + [sequence for sequence in fossil_sequences if paths[sequence] == 1] + [sequence for sequence in fossil_sequences if paths[sequence] == 2]
    # If it is not possible to find two evolutionary paths in the fossil record, return the word "impossible"
    else:
        return "impossible"



def f1(n, current_sequence, *fossil_sequences):
    # Initialize a dictionary to store the evolutionary paths
    paths = {}

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is already in the dictionary
        if sequence not in paths:
            # If not, add it to the dictionary with a value of 1
            paths[sequence] = 1
        else:
            # If it is already in the dictionary, increment its value
            paths[sequence] += 1

    # Initialize two lists to store the sequences for the two evolutionary paths
    path1 = []
    path2 = []

    # Iterate through the dictionary
    for sequence, count in paths.items():
        # Check if the sequence is in the current sequence
        if sequence in current_sequence:
            # If it is, add it to the first path
            path1.append(sequence)
        else:
            # If it is not, add it to the second path
            path2.append(sequence)

    # Return the two lists of sequences
    return path1, path2

def f2(n, current_sequence, *fossil_sequences):
    # Initialize a dictionary to store the evolutionary paths
    paths = {}

    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is already in the dictionary
        if sequence not in paths:
            # If not, add it to the dictionary with a value of 1
            paths[sequence] = 1
        else:
            # If it is already in the dictionary, increment its value
            paths[sequence] += 1

    # Initialize two lists to store the sequences for the two evolutionary paths
    path1 = []
    path2 = []

    # Iterate through the dictionary
    for sequence, count in paths.items():
        # Check if the sequence is in the current sequence
        if sequence in current_sequence:
            # If it is, add it to the first path
            path1.append(sequence)
        else:
            # If it is not, add it to the second path
            path2.append(sequence)

    # Return the two lists of sequences
    return path1, path2

if __name__ == '__main__':
    n = int(input())
    current_sequence = input()
    fossil_sequences = [input() for _ in range(n)]
    path1, path2 = f1(n, current_sequence, *fossil_sequences)
    print(len(path1), len(path2))
    for sequence in path1:
        print(sequence)
    for sequence in path2:
        print(sequence)


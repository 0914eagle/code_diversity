
def solve(n, current_sequence, fossil_sequences):
    # Initialize a dictionary to store the nucleotide counts for each path
    path1_counts = {}
    path2_counts = {}
    
    # Iterate through the fossil sequences
    for sequence in fossil_sequences:
        # Check if the sequence is in the current sequence
        if sequence in current_sequence:
            # If it is, add it to the first path
            path1_counts[sequence] = path1_counts.get(sequence, 0) + 1
        else:
            # If it's not, add it to the second path
            path2_counts[sequence] = path2_counts.get(sequence, 0) + 1
    
    # Initialize variables to store the number of sequences in each path
    path1_sequences = 0
    path2_sequences = 0
    
    # Iterate through the nucleotide counts for each path
    for sequence, count in path1_counts.items():
        # If the count is greater than 0, add the sequence to the first path
        if count > 0:
            path1_sequences += 1
    
    for sequence, count in path2_counts.items():
        # If the count is greater than 0, add the sequence to the second path
        if count > 0:
            path2_sequences += 1
    
    # Check if it is possible to have two evolutionary paths
    if path1_sequences > 0 and path2_sequences > 0:
        # If it is, return the number of sequences in each path and the sequences themselves
        return path1_sequences, path1_counts, path2_sequences, path2_counts
    else:
        # If it's not, return the word "impossible"
        return "impossible"


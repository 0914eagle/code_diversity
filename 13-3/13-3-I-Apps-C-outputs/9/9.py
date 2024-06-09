
import itertools

def count_sequences(N, C):
    # Initialize a list to store the sequences
    sequences = []
    
    # Iterate over all possible sequences of length N
    for seq in itertools.permutations(range(1, N+1)):
        # Calculate the confusion of the current sequence
        confusion = 0
        for i in range(N-1):
            if seq[i] > seq[i+1]:
                confusion += 1
        
        # If the confusion is equal to C, add the sequence to the list
        if confusion == C:
            sequences.append(seq)
    
    # Return the number of sequences modulo 1000000007
    return len(sequences) % 1000000007


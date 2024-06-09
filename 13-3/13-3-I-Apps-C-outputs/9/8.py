
import itertools

def count_confused_sequences(n, c):
    # Initialize a list to store the sequences
    sequences = []
    
    # Iterate over all possible sequences of length n
    for seq in itertools.permutations(range(1, n+1)):
        # Count the number of confused pairs in the sequence
        confused_pairs = 0
        for i in range(n-1):
            if seq[i] > seq[i+1]:
                confused_pairs += 1
        
        # If the number of confused pairs is equal to c, add the sequence to the list
        if confused_pairs == c:
            sequences.append(seq)
    
    # Return the number of sequences modulo 1000000007
    return len(sequences) % 1000000007


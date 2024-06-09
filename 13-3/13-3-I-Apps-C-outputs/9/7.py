
import itertools

def count_sequences(n, c):
    # Initialize a list to store the sequences
    sequences = []
    
    # Iterate over all possible sequences of length n
    for seq in itertools.permutations(range(1, n + 1)):
        # Initialize a variable to store the number of confused pairs
        confused_pairs = 0
        
        # Iterate over all pairs of numbers in the sequence
        for i in range(n - 1):
            # If the number that comes earlier in the sequence is larger than the later number, increment the number of confused pairs
            if seq[i] > seq[i + 1]:
                confused_pairs += 1
        
        # If the number of confused pairs is equal to c, add the sequence to the list of sequences
        if confused_pairs == c:
            sequences.append(seq)
    
    # Return the number of sequences modulo 1000000007
    return len(sequences) % 1000000007


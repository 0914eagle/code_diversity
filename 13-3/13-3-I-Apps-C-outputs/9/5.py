
import itertools

def get_confused_sequences(n, c):
    # Initialize a list to store the sequences
    sequences = []
    
    # Iterate over all possible sequences of length n
    for seq in itertools.permutations(range(1, n+1)):
        # Calculate the confusion of the current sequence
        confusion = 0
        for i in range(n-1):
            if seq[i] > seq[i+1]:
                confusion += 1
        
        # If the confusion is equal to c, add the sequence to the list of sequences
        if confusion == c:
            sequences.append(seq)
    
    # Return the number of sequences modulo 1000000007
    return len(sequences) % 1000000007

n, c = map(int, input().split())
print(get_confused_sequences(n, c))


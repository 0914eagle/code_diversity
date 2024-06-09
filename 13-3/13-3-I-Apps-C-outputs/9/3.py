
import itertools

def count_confused_sequences(n, c):
    # Initialize a list to store the confused sequences
    confused_sequences = []
    
    # Iterate over all possible sequences of length n
    for sequence in itertools.permutations(range(1, n + 1)):
        # Calculate the confusion of the current sequence
        confusion = 0
        for i in range(n - 1):
            if sequence[i] > sequence[i + 1]:
                confusion += 1
        
        # If the confusion is equal to c, add the sequence to the list of confused sequences
        if confusion == c:
            confused_sequences.append(sequence)
    
    # Return the number of confused sequences
    return len(confused_sequences)

# Test the function with the sample input
n = 10
c = 1
print(count_confused_sequences(n, c)) # Should print 9

n = 4
c = 3
print(count_confused_sequences(n, c)) # Should print 6


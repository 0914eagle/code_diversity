
import itertools

def number_of_unsorted_sequences(n, a):
    # Initialize a counter for the number of unsorted sequences
    count = 0
    
    # Iterate over all possible permutations of the input sequence
    for perm in itertools.permutations(a):
        # Check if the current permutation is entirely unsorted
        if all(perm[i] != i for i in range(n)):
            # Increment the counter
            count += 1
    
    # Return the result modulo 10^9 + 9
    return count % 1000000009


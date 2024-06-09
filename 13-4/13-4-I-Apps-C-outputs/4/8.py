
def solve(n, m):
    # Calculate the number of possible sequences
    num_sequences = 2**n
    
    # Initialize a set to store the indices of wool sequences
    wool_sequences = set()
    
    # Iterate over all possible lengths of wool sequences
    for l in range(1, n+1):
        # Iterate over all possible starting indices
        for i in range(n-l+1):
            # Calculate the xor of the sequence
            xor = 0
            for j in range(l):
                xor ^= i+j
            
            # If the xor is 0, add the sequence to the set of wool sequences
            if xor == 0:
                wool_sequences.add(i)
    
    # Return the number of sequences that are not wool sequences
    return num_sequences - len(wool_sequences) % 1000000009



def solve(n, m):
    # Calculate the total number of sequences
    total_sequences = 2**n
    
    # Initialize a set to store the indices of wool sequences
    wool_sequences = set()
    
    # Iterate over all possible lengths of wool sequences
    for l in range(1, n+1):
        # Iterate over all possible starting indices
        for i in range(n-l+1):
            # Calculate the ending index
            j = i + l - 1
            # Check if the xor of the sequence is 0
            if xor_sequence(i, j, n) == 0:
                # Add the indices to the set of wool sequences
                wool_sequences.add(i)
                wool_sequences.add(j)
    
    # Calculate the number of non-wool sequences
    non_wool_sequences = total_sequences - len(wool_sequences)
    
    # Return the result modulo 1000000009
    return non_wool_sequences % 1000000009

def xor_sequence(i, j, n):
    # Initialize the xor of the sequence to 0
    xor = 0
    # Iterate over the indices of the sequence
    for k in range(i, j+1):
        # Calculate the xor of the current element with the previous xor
        xor ^= k
    # Return the xor of the sequence
    return xor


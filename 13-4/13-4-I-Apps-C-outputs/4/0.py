
def solve(n, m):
    # Initialize a set to store the wool sequences
    wool_sequences = set()
    
    # Iterate over all possible sequences of length n
    for i in range(2**n):
        # Convert the binary representation of i to a list of integers
        seq = [int(j) for j in bin(i)[2:]]
        
        # Check if the sequence is a wool sequence
        if is_wool_sequence(seq):
            # If it is, add it to the set of wool sequences
            wool_sequences.add(tuple(seq))
    
    # Initialize a set to store the non-wool sequences
    non_wool_sequences = set()
    
    # Iterate over all possible sequences of length n
    for i in range(2**n):
        # Convert the binary representation of i to a list of integers
        seq = [int(j) for j in bin(i)[2:]]
        
        # Check if the sequence is not a wool sequence
        if seq not in wool_sequences:
            # If it is, add it to the set of non-wool sequences
            non_wool_sequences.add(tuple(seq))
    
    # Return the number of non-wool sequences
    return len(non_wool_sequences) % 1000000009

# Check if a sequence is a wool sequence
def is_wool_sequence(seq):
    # Initialize a variable to store the xor of the sequence
    xor = 0
    
    # Iterate over the sequence
    for i in range(len(seq)):
        # Update the xor with the current element
        xor ^= seq[i]
    
    # Check if the xor is 0
    return xor == 0



def get_good_sequences(n, a):
    # Initialize a set to store the good sequences
    good_sequences = set()
    
    # Iterate over each possible length of the sequence
    for length in range(1, n + 1):
        # Iterate over each possible starting index of the sequence
        for start in range(n - length + 1):
            # Get the sequence of numbers
            sequence = a[start:start + length]
            # Check if the sequence is good
            if is_good_sequence(sequence):
                # Add the sequence to the set of good sequences
                good_sequences.add(tuple(sequence))
    
    # Return the number of good sequences
    return len(good_sequences)

def is_good_sequence(sequence):
    # Initialize a variable to store the result
    result = True
    
    # Iterate over each number in the sequence
    for i in range(len(sequence) - 1):
        # Get the bitwise exclusive or of the current number and the next number
        xor = sequence[i] ^ sequence[i + 1]
        # Check if the result is not zero
        if xor != 0:
            # The sequence is not good, return False
            return False
    
    # The sequence is good, return True
    return True

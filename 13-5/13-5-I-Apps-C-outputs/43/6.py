
def get_valid_sequence(n, k):
    # Initialize a list to store the valid sequences
    valid_sequences = []
    
    # Iterate through all possible sequences of length n-1
    for seq in itertools.product(range(1, n), repeat=n-1):
        # Check if the sequence is valid
        if not is_valid_sequence(seq, n):
            continue
        # Add the sequence to the list of valid sequences
        valid_sequences.append(seq)
    
    # Return the kth valid sequence
    return valid_sequences[k-1]

def is_valid_sequence(seq, n):
    # Initialize a flag to indicate if the sequence is valid
    valid = True
    
    # Iterate through the sequence and check if the total number of petals is a multiple of n
    for i in range(len(seq)):
        if sum(seq[:i+1]) % n == 0:
            valid = False
            break
    
    # Return the flag
    return valid

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_valid_sequence(n, k))


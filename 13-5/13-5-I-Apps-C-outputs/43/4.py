
def f1(n, k):
    # Initialize a list to store the valid sequences
    valid_sequences = []
    
    # Iterate through all possible sequences of length n-1
    for seq in itertools.product(range(1, n), repeat=n-1):
        # Check if the sequence is valid by checking if the total number of petals is not a multiple of n
        if sum(seq) % n != 0:
            valid_sequences.append(seq)
    
    # Return the kth valid sequence
    return valid_sequences[k-1]

def f2(n, k):
    # Initialize a list to store the valid sequences
    valid_sequences = []
    
    # Iterate through all possible sequences of length n-1
    for seq in itertools.product(range(1, n), repeat=n-1):
        # Check if the sequence is valid by checking if the total number of petals is not a multiple of n
        if sum(seq) % n != 0:
            valid_sequences.append(seq)
    
    # Return the kth valid sequence
    return valid_sequences[k-1]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(f1(n, k))
    print(f2(n, k))


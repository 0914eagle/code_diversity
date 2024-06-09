
def longest_monotone_subsequence(N, K):
    # Initialize a list to store the required sequence
    seq = []
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # If the length of the sequence is less than K, append the current number to the sequence
        if len(seq) < K:
            seq.append(i)
        # If the length of the sequence is equal to K, check if the current number is the opposite of the last number in the sequence
        elif len(seq) == K:
            # If the current number is the opposite of the last number in the sequence, append it to the sequence
            if seq[-1] != i:
                seq.append(i)
            # If the current number is not the opposite of the last number in the sequence, return -1 as the required sequence doesn't exist
            else:
                return -1
    
    # If the required sequence exists, return it
    return seq


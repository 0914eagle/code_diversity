
def longest_monotone_subsequence(N, K):
    # Initialize a list to store the required sequence
    seq = []
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # If the length of the current sequence is less than K, add the current number to the sequence
        if len(seq) < K:
            seq.append(i)
        # If the length of the current sequence is equal to K, remove the first number from the sequence and add the current number to the end
        elif len(seq) == K:
            seq.pop(0)
            seq.append(i)
    
    # If the length of the sequence is not equal to N, it means that a valid sequence does not exist
    if len(seq) != N:
        return -1
    
    return " ".join(str(x) for x in seq)


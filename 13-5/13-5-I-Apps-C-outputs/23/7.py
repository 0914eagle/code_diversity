
def find_longest_monotone_subsequence(N, K):
    # Initialize a list to store the required sequence
    seq = []
    
    # Initialize a set to keep track of the numbers that have been used
    used_numbers = set()
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # If the current number has not been used and the length of the sequence is less than or equal to K,
        if i not in used_numbers and len(seq) <= K:
            # Add the current number to the sequence and mark it as used
            seq.append(i)
            used_numbers.add(i)
        # If the current number has been used or the length of the sequence is greater than K,
        else:
            # Find the first number in the sequence that has not been used and remove it
            for j in range(len(seq)):
                if seq[j] not in used_numbers:
                    used_numbers.remove(seq[j])
                    break
            # Add the current number to the sequence and mark it as used
            seq.append(i)
            used_numbers.add(i)
    
    # If the length of the sequence is not equal to N, return -1
    if len(seq) != N:
        return -1
    
    # Return the required sequence
    return seq


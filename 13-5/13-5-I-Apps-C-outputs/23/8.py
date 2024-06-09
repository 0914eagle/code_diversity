
def find_longest_monotone_subsequence(N, K):
    # Initialize a list to store the required sequence
    seq = []
    
    # Initialize a set to keep track of the numbers that have been used
    used_numbers = set()
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # If the length of the sequence is less than K, append the current number to the sequence
        if len(seq) < K:
            seq.append(i)
            used_numbers.add(i)
        # If the length of the sequence is equal to K, check if the current number is not in the used_numbers set
        elif i not in used_numbers:
            # If the current number is not in the used_numbers set, append it to the sequence and add it to the used_numbers set
            seq.append(i)
            used_numbers.add(i)
        # If the length of the sequence is greater than K, remove the first element from the sequence and add the current number to the used_numbers set
        else:
            seq.pop(0)
            seq.append(i)
            used_numbers.add(i)
    
    # If the length of the sequence is not equal to N, return -1
    if len(seq) != N:
        return -1
    
    # Return the required sequence
    return seq


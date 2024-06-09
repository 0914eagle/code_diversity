
def find_sequence(n, k):
    if k > n or k < 1:
        return -1
    
    sequence = list(range(1, n+1))
    while True:
        longest_monotone_subsequence = 0
        for i in range(n):
            current_subsequence = 1
            for j in range(i+1, n):
                if sequence[i] < sequence[j]:
                    current_subsequence += 1
                else:
                    break
            longest_monotone_subsequence = max(longest_monotone_subsequence, current_subsequence)
        
        if longest_monotone_subsequence == k:
            return sequence
        
        # If the longest monotone subsequence is not equal to k,
        # then we need to modify the sequence to create a longer monotone subsequence.
        # We can do this by swapping two elements in the sequence.
        # Find the two elements that are farthest from each other and swap them.
        farthest_index_1 = 0
        farthest_index_2 = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if sequence[j] - sequence[i] > sequence[farthest_index_2] - sequence[farthest_index_1]:
                    farthest_index_1 = i
                    farthest_index_2 = j
        
        sequence[farthest_index_1], sequence[farthest_index_2] = sequence[farthest_index_2], sequence[farthest_index_1]


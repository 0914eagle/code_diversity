
def get_good_sequences(n, a):
    # Initialize a set to store the pairs (l, r) that satisfy the condition
    pairs = set()
    
    # Loop through each pair of integers (l, r) such that 1 <= l <= r <= n
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a variable to store the result of bitwise XOR of all elements in the sequence a[l], a[l + 1], ..., a[r]
            result = 0
            
            # Loop through each element in the sequence a[l], a[l + 1], ..., a[r]
            for i in range(l, r + 1):
                # Perform bitwise XOR of the result with the current element
                result ^= a[i]
            
            # If the result is 0, it means that the sequence is good, so add the pair (l, r) to the set of pairs
            if result == 0:
                pairs.add((l, r))
    
    # Return the number of pairs in the set
    return len(pairs)


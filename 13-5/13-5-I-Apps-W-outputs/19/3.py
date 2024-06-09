
def solve(n, a):
    # Initialize a set to store the pairs (l, r) that satisfy the condition
    pairs = set()
    
    # Iterate over each pair of integers (l, r) such that 1 <= l <= r <= n
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a variable to store the result of bitwise exclusive or of all elements in the sequence a[l], a[l+1], ..., a[r]
            result = 0
            
            # Iterate over each element in the sequence a[l], a[l+1], ..., a[r]
            for i in range(l, r + 1):
                # Calculate the bitwise exclusive or of the current element with the result
                result ^= a[i - 1]
            
            # If the result is equal to 0, it means that the sequence is good, so we add the pair (l, r) to the set of pairs
            if result == 0:
                pairs.add((l, r))
    
    # Return the length of the set of pairs
    return len(pairs)


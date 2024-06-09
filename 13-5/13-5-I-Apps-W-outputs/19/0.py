
def solve(n, a):
    # Initialize a set to store the pairs (l, r)
    pairs = set()
    
    # Iterate over each pair of integers (l, r) such that 1 <= l <= r <= n
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a variable to store the result of bitwise exclusive or of all elements
            result = 0
            
            # Iterate over each element a[i] such that l <= i <= r
            for i in range(l, r + 1):
                # Perform bitwise exclusive or of result and a[i]
                result ^= a[i - 1]
            
            # If the result is equal to 0, then (l, r) is a valid pair
            if result == 0:
                pairs.add((l, r))
    
    # Return the number of pairs
    return len(pairs)


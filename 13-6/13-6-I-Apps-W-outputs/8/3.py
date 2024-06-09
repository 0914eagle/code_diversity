
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the result
    result = [0]
    
    # Iterate over all possible permutations
    for perm in itertools.permutations(range(1, n + 1)):
        # Check if the permutation is an almost identity permutation
        if sum(1 for i, x in enumerate(perm, 1) if x == i) >= n - k:
            # Increment the result if it is an almost identity permutation
            result[0] += 1
    
    # Return the result
    return result[0]


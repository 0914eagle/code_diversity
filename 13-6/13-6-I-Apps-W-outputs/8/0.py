
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the result
    result = [0]
    
    # Iterate over all possible permutations
    for perm in itertools.permutations(range(1, n+1)):
        # Check if the permutation is an almost identity permutation
        if sum(1 for i, x in enumerate(perm) if x == i) >= n - k:
            # If it is, add it to the result
            result.append(perm)
    
    # Return the number of almost identity permutations
    return len(result)


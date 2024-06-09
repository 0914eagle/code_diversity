
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the almost identity permutations
    almost_identity_permutations = []

    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Check if the permutation is an almost identity permutation
        if len(set(permutation)) == n:
            almost_identity_permutations.append(permutation)

    # Return the number of almost identity permutations
    return len(almost_identity_permutations)


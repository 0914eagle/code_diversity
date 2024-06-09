
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the almost identity permutations
    almost_identity_permutations = []

    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Count the number of indices i such that permutation[i] == i
        num_identical = sum(1 for i in range(n) if permutation[i] == i)

        # If the number of identical indices is greater than or equal to k,
        # then the permutation is an almost identity permutation
        if num_identical >= k:
            almost_identity_permutations.append(permutation)

    # Return the number of almost identity permutations
    return len(almost_identity_permutations)


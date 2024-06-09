
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the almost identity permutations
    almost_identity_permutations = []

    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list
        permutation_list = list(permutation)

        # Count the number of indices i such that permutation_list[i] = i
        num_identical_indices = 0
        for i in range(n):
            if permutation_list[i] == i + 1:
                num_identical_indices += 1

        # If the number of identical indices is greater than or equal to k,
        # then the permutation is an almost identity permutation
        if num_identical_indices >= k:
            almost_identity_permutations.append(permutation)

    # Return the number of almost identity permutations
    return len(almost_identity_permutations)


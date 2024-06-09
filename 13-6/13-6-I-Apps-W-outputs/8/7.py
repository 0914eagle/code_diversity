
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the almost identity permutations
    almost_identity_permutations = []

    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list
        permutation_list = list(permutation)

        # Count the number of indices where the value is equal to the index
        num_equal_indices = 0
        for i in range(n):
            if permutation_list[i] == i + 1:
                num_equal_indices += 1

        # If the number of equal indices is greater than or equal to k, add the permutation to the list
        if num_equal_indices >= k:
            almost_identity_permutations.append(permutation_list)

    # Return the length of the list of almost identity permutations
    return len(almost_identity_permutations)


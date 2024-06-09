
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the almost identity permutations
    almost_identity_permutations = []

    # Iterate over all possible permutations
    for permutation in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list
        permutation_list = list(permutation)

        # Count the number of indices i such that permutation[i] = i
        num_identities = 0
        for i in range(n):
            if permutation_list[i] == i + 1:
                num_identities += 1

        # If the number of identities is greater than or equal to k, add the permutation to the list of almost identity permutations
        if num_identities >= k:
            almost_identity_permutations.append(permutation_list)

    # Return the length of the list of almost identity permutations
    return len(almost_identity_permutations)


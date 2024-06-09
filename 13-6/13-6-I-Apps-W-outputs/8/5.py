
def count_almost_identity_permutations(n, k):
    # Initialize a list to store the result
    result = [0]

    # Iterate over all possible permutations
    for perm in itertools.permutations(range(1, n + 1)):
        # Count the number of indices i such that perm[i] = i
        count = 0
        for i in range(n):
            if perm[i] == i + 1:
                count += 1

        # If the number of indices is greater than or equal to k, add the permutation to the result
        if count >= k:
            result.append(perm)

    # Return the number of almost identity permutations
    return len(result)


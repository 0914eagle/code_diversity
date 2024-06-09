
def permutation_sum(n):
    # Initialize a list to store the results
    results = []

    # Iterate over all possible permutations of length n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Check if the sum of the permutations is valid
            if (i + j) % n == 0:
                # Add the pair of permutations to the results
                results.append((i, j))

    # Return the number of distinct pairs of permutations
    return len(set(results))


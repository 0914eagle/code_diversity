
def permutation_sum(n):
    # Initialize a list to store the results
    result = []

    # Iterate over all possible permutations of length n
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # Check if the sum of a and b is a valid permutation
            if (a + b) % n == 0:
                result.append((a, b))

    # Return the number of distinct pairs of permutations
    return len(result)


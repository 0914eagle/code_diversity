
def count_permutations(n, k, p):
    # Initialize the number of permutations to 1
    num_permutations = 1

    # Iterate over each element in the permutation
    for i in range(n):
        # If the element is not the first element in the permutation,
        # we need to consider the previous elements as well
        if i > 0:
            # Get the number of permutations for the previous elements
            num_permutations = (num_permutations * (n - i)) % p

        # Get the number of permutations for the current element
        num_permutations = (num_permutations * k) % p

    return num_permutations


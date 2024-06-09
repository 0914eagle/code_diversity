
def get_magical_permutation(S):
    # Find the largest power of 2 that is less than or equal to the length of S
    max_power = 1
    while max_power < len(S):
        max_power *= 2
    max_power //= 2

    # Initialize the magical permutation with the first element of S
    permutation = [S[0]]

    # Iterate through the remaining elements of S
    for i in range(1, len(S)):
        # Find the next element of the permutation that is not already in the permutation
        next_element = S[i]
        while next_element in permutation:
            next_element = (next_element + 1) % len(S)

        # Add the next element to the permutation
        permutation.append(next_element)

    # Return the magical permutation
    return permutation


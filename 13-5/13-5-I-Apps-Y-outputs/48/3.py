
def solve(N, K, d, A):
    # Initialize a set to store the indices of the Snukes who have no snacks
    no_snacks = set()

    # Iterate over the input data
    for i in range(K):
        # Check if the current Snack has any Snukes who have not eaten it yet
        if len(set(A[i]) - no_snacks) > 0:
            # If so, add the indices of the Snukes who have not eaten it yet to the set
            no_snacks |= set(A[i])
        else:
            # If not, add the indices of the Snukes who have eaten it to the set
            no_snacks |= set(A[i])

    # Return the number of Snukes who have no snacks
    return len(no_snacks)


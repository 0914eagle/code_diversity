
def solve(N, K, d, A):
    # Initialize a set to store the snukes with no snacks
    no_snacks = set()

    # Iterate over each kind of snack
    for i in range(K):
        # Iterate over each snuke that has this snack
        for j in range(d[i]):
            # Add the snuke to the set of snukes with no snacks
            no_snacks.add(A[i][j])

    # Return the number of snukes with no snacks
    return len(no_snacks)


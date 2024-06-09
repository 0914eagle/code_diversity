
def solve(N, K, d, A):
    # Initialize a set to store the snukes who have no snacks
    no_snacks = set()

    # Iterate over each kind of snack
    for i in range(K):
        # Iterate over each snuke who has this snack
        for j in range(d[i]):
            # Add the snuke to the set of snukes who have no snacks
            no_snacks.add(A[i][j])

    # Return the number of snukes who have no snacks
    return len(no_snacks)


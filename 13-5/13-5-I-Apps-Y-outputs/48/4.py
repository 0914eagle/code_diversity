
def solve(n, k, d, a):
    # Initialize a set to store the snukes who have no snacks
    no_snacks = set()

    # Iterate over each kind of snack
    for i in range(k):
        # Iterate over each snuke who has this snack
        for j in range(d[i]):
            # Add the snuke to the set of no snacks
            no_snacks.add(a[i][j])

    # Return the length of the set of no snacks
    return len(no_snacks)


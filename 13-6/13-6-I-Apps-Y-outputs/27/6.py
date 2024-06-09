
def solve(n, k, d, a):
    # Initialize a set to store the snukes with no snacks
    no_snacks = set()
    
    # Iterate over the input data
    for i in range(k):
        # Check if the current snack is not in the set of snukes with no snacks
        if i not in no_snacks:
            # Iterate over the snukes that have the current snack
            for j in range(d[i]):
                # Add the current snukes to the set of snukes with no snacks
                no_snacks.add(a[i][j])
    
    # Return the number of snukes with no snacks
    return len(no_snacks)


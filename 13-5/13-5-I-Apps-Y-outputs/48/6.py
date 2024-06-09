
def solve(snukes, snacks):
    # Initialize a set to store the snukes with no snacks
    no_snacks = set()

    # Iterate over the snukes and snacks
    for snukes, snacks in enumerate(snacks):
        # If the snukes has no snacks, add it to the set
        if not snacks:
            no_snacks.add(snukes)

    # Return the length of the set
    return len(no_snacks)


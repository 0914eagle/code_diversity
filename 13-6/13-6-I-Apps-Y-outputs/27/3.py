
def solve(snukes, snacks):
    # Initialize a set to store the snukes with no snacks
    no_snacks = set()

    # Iterate over the snukes and their snacks
    for snuke, snack_list in enumerate(snacks, start=1):
        # If the snuke has no snacks, add it to the set
        if not snack_list:
            no_snacks.add(snuke)

    # Return the number of snukes with no snacks
    return len(no_snacks)


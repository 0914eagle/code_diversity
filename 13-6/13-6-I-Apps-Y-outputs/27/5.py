
def solve(snukes, snacks):
    # Initialize a set to store the snukes who have no snacks
    no_snacks = set()
    
    # Iterate over the snukes and their snacks
    for snukes, snacks in snacks:
        # If the snukes has no snacks, add it to the set
        if not snacks:
            no_snacks.add(snukes)
    
    # Return the number of snukes who have no snacks
    return len(no_snacks)


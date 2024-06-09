
def solve(n, k, d, snacks):
    # Initialize a set to store the snukes with no snacks
    no_snacks = set()
    
    # Iterate over the snacks and add the snukes with no snacks to the set
    for i in range(k):
        for snuk in snacks[i]:
            if snuk not in no_snacks:
                no_snacks.add(snuk)
    
    # Return the number of snukes with no snacks
    return len(no_snacks)


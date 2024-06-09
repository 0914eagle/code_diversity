
def get_smallest_pack(B, k, companies):
    # Initialize a dictionary to store the minimum number of bolts required to buy a pack
    min_bolts_required = {}
    # Initialize a dictionary to store the number of bolts in each pack
    num_bolts = {}
    # Loop through each company
    for i in range(k):
        # Get the number of types of packages and their sizes
        l, *sizes = companies[i]
        # Loop through each type of package
        for j in range(l):
            # Get the number of bolts in the package
            n = sizes[j]
            # If the number of bolts is less than or equal to the number of bolts required, add it to the minimum number of bolts required dictionary
            if n <= B:
                min_bolts_required[n] = min(min_bolts_required.get(n, float('inf')), n)
            # Add the number of bolts to the total number of bolts dictionary
            num_bolts[n] = num_bolts.get(n, 0) + n
    
    # Loop through the minimum number of bolts required dictionary and find the smallest key that is greater than or equal to the number of bolts required
    for n in sorted(min_bolts_required):
        if n >= B:
            return n
    
    # If no key is found, return impossible
    return "impossible"


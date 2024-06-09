
def solve(B, k, companies):
    # Initialize a dictionary to store the minimum amount of bolts required to buy B bolts
    min_bolts_required = {}
    # Initialize a dictionary to store the number of bolts in each pack
    num_bolts_in_pack = {}
    # Initialize a dictionary to store the number of packs required to buy B bolts
    num_packs_required = {}
    
    # Loop through each company
    for i in range(k):
        # Get the number of pack types and their sizes for the current company
        l, *pack_sizes = companies[i]
        # Loop through each pack type
        for j in range(l):
            # Get the number of bolts in the current pack type
            num_bolts = pack_sizes[j]
            # Check if the current pack type is the smallest pack type that contains at least B bolts
            if num_bolts >= B:
                # If it is, return the size of the pack
                return num_bolts
            # If the current pack type is not the smallest pack type that contains at least B bolts, store the minimum amount of bolts required to buy B bolts
            min_bolts_required[i] = num_bolts
    
    # If no pack type contains at least B bolts, return "impossible"
    return "impossible"


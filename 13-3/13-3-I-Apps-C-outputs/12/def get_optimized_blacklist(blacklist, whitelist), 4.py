
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist as an empty set
    optimized_blacklist = set()

    # Iterate over the blacklist and whitelist
    for subnet in blacklist:
        # If the subnet is not in the whitelist, add it to the optimized blacklist
        if subnet not in whitelist:
            optimized_blacklist.add(subnet)

    # Return the optimized blacklist
    return optimized_blacklist


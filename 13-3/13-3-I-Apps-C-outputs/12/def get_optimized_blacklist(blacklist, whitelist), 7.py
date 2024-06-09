
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist as an empty list
    optimized_blacklist = []

    # Iterate over the blacklist and whitelist
    for blacklist_subnet in blacklist:
        for whitelist_subnet in whitelist:
            # Check if the blacklist subnet and whitelist subnet intersect
            if blacklist_subnet.intersects(whitelist_subnet):
                # If they intersect, return -1 as the solution is not unique
                return -1

    # If the blacklist and whitelist do not intersect, add the blacklist subnets to the optimized blacklist
    optimized_blacklist.extend(blacklist)

    # Return the optimized blacklist
    return optimized_blacklist


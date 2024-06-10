
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist with an empty list
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

def get_blacklist_subnets(subnets):
    # Initialize the blacklist with an empty list
    blacklist = []

    # Iterate over the subnets
    for subnet in subnets:
        # Check if the subnet is blacklisted
        if subnet.startswith("-"):
            # If it is, add it to the blacklist
            blacklist.append(subnet[1:])

    # Return the blacklist
    return blacklist

def get_whitelist_subnets(subnets):
    # Initialize the whitelist with an empty list
    whitelist = []

    # Iterate over the subnets
    for subnet in subnets:
        # Check if the subnet is whitelisted
        if subnet.startswith("+"):
            # If it is, add it to the whitelist
            whitelist.append(subnet[1:])

    # Return the whitelist
    return whitelist

def main():
    # Read the number of subnets
    n = int(input())

    # Read the subnets
    subnets = []
    for _ in range(n):
        subnets.append(input())

    # Get the blacklist and whitelist subnets
    blacklist = get_blacklist_subnets(subnets)
    whitelist = get_whitelist_subnets(subnets)

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # Print the optimized blacklist
    print(len(optimized_blacklist))
    for subnet in optimized_blacklist:
        print(subnet)

if __name__ == '__main__':
    main()



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

def get_blacklist_from_subnets(subnets):
    # Initialize the blacklist as an empty set
    blacklist = set()

    # Iterate over the subnets
    for subnet in subnets:
        # If the subnet is a blacklist subnet, add it to the blacklist
        if subnet.startswith("-"):
            blacklist.add(subnet[1:])

    # Return the blacklist
    return blacklist

def get_whitelist_from_subnets(subnets):
    # Initialize the whitelist as an empty set
    whitelist = set()

    # Iterate over the subnets
    for subnet in subnets:
        # If the subnet is a whitelist subnet, add it to the whitelist
        if subnet.startswith("+"):
            whitelist.add(subnet[1:])

    # Return the whitelist
    return whitelist

def get_subnets_from_input(input_file):
    # Read the input file
    with open(input_file, "r") as f:
        # Get the number of subnets
        n = int(f.readline())

        # Initialize the subnets as an empty list
        subnets = []

        # Iterate over the lines of the input file
        for line in f:
            # Add the subnet to the subnets list
            subnets.append(line.strip())

    # Return the subnets
    return subnets

def main():
    # Get the subnets from the input file
    subnets = get_subnets_from_input("input.txt")

    # Get the blacklist and whitelist from the subnets
    blacklist = get_blacklist_from_subnets(subnets)
    whitelist = get_whitelist_from_subnets(subnets)

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # Print the optimized blacklist
    print(len(optimized_blacklist))
    for subnet in optimized_blacklist:
        print(subnet)

if __name__ == '__main__':
    main()


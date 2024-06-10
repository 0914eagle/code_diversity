
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist as an empty list
    optimized_blacklist = []

    # Iterate over the blacklist and whitelist
    for blacklist_subnet in blacklist:
        for whitelist_subnet in whitelist:
            # Check if the blacklist subnet and whitelist subnet intersect
            if blacklist_subnet.intersects(whitelist_subnet):
                # If they intersect, return -1
                return -1

    # If no intersection is found, add the blacklist subnet to the optimized blacklist
    optimized_blacklist.append(blacklist_subnet)

    # Return the optimized blacklist
    return optimized_blacklist

def main():
    # Read the number of subnets from stdin
    n = int(input())

    # Initialize the blacklist and whitelist as empty lists
    blacklist = []
    whitelist = []

    # Iterate over the number of subnets
    for _ in range(n):
        # Read the subnet from stdin
        subnet = input()

        # Check if the subnet is in the blacklist
        if subnet.startswith("-"):
            # If it is, add it to the blacklist
            blacklist.append(subnet[1:])
        # Check if the subnet is in the whitelist
        elif subnet.startswith("+"):
            # If it is, add it to the whitelist
            whitelist.append(subnet[1:])

    # Call the get_optimized_blacklist function and print the result
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)
    print(len(optimized_blacklist))
    for subnet in optimized_blacklist:
        print(subnet)

if __name__ == '__main__':
    main()


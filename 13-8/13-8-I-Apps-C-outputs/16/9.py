
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist with the blacklist
    optimized_blacklist = blacklist.copy()

    # Iterate over the whitelist and remove any subnets that are also in the blacklist
    for subnet in whitelist:
        if subnet in optimized_blacklist:
            optimized_blacklist.remove(subnet)

    # Return the optimized blacklist
    return optimized_blacklist

def get_intersection(blacklist, whitelist):
    # Initialize the intersection as an empty set
    intersection = set()

    # Iterate over the blacklist and whitelist and add any common subnets to the intersection
    for subnet in blacklist:
        if subnet in whitelist:
            intersection.add(subnet)

    # Return the intersection
    return intersection

def main():
    # Read the number of subnets from stdin
    n = int(input())

    # Read the subnets from stdin
    blacklist = set()
    whitelist = set()
    for _ in range(n):
        subnet = input()
        if subnet.startswith("-"):
            blacklist.add(subnet[1:])
        else:
            whitelist.add(subnet)

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # Get the intersection of the blacklist and whitelist
    intersection = get_intersection(blacklist, whitelist)

    # Check if there is an IPv4 address that matches both the whitelist and the blacklist
    if len(intersection) > 0:
        print(-1)
    else:
        # Print the length of the optimized blacklist
        print(len(optimized_blacklist))

        # Print the optimized blacklist
        for subnet in optimized_blacklist:
            print(subnet)

if __name__ == '__main__':
    main()


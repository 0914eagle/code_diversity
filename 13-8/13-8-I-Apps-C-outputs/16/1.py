
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist with the blacklist
    optimized_blacklist = blacklist.copy()

    # Iterate through the whitelist
    for subnet in whitelist:
        # If the subnet is already in the optimized blacklist, remove it
        if subnet in optimized_blacklist:
            optimized_blacklist.remove(subnet)

    # Return the optimized blacklist
    return optimized_blacklist

def get_intersection(blacklist, whitelist):
    # Initialize the intersection as an empty set
    intersection = set()

    # Iterate through the blacklist
    for subnet in blacklist:
        # If the subnet is also in the whitelist, add it to the intersection
        if subnet in whitelist:
            intersection.add(subnet)

    # Return the intersection
    return intersection

def main():
    # Read the number of subnets
    n = int(input())

    # Initialize the blacklist and whitelist as empty sets
    blacklist = set()
    whitelist = set()

    # Read the subnets
    for _ in range(n):
        # Read the sign and subnet
        sign, subnet = input().split()

        # Add the subnet to the appropriate list
        if sign == "-":
            blacklist.add(subnet)
        elif sign == "+":
            whitelist.add(subnet)

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # Get the intersection of the blacklist and whitelist
    intersection = get_intersection(blacklist, whitelist)

    # If the intersection is not empty, return -1
    if len(intersection) > 0:
        print(-1)
    # Otherwise, return the length of the optimized blacklist and the subnets
    else:
        print(len(optimized_blacklist))
        for subnet in optimized_blacklist:
            print(subnet)

if __name__ == '__main__':
    main()


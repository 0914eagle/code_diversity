
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimised blacklist with the blacklist
    optimized_blacklist = set(blacklist)

    # Iterate through the whitelist and remove any overlapping subnets from the optimised blacklist
    for subnet in whitelist:
        optimized_blacklist.discard(subnet)

    # Return the optimised blacklist
    return optimized_blacklist

def get_intersection(blacklist, whitelist):
    # Initialize the intersection as an empty set
    intersection = set()

    # Iterate through the blacklist and check if any subnets overlap with the whitelist
    for subnet in blacklist:
        if subnet in whitelist:
            intersection.add(subnet)

    # Return the intersection
    return intersection

def main():
    # Read the number of subnets from stdin
    n = int(input())

    # Initialize the blacklist and whitelist as empty sets
    blacklist = set()
    whitelist = set()

    # Read the subnets from stdin and add them to the appropriate list
    for _ in range(n):
        sign, subnet = input().split()
        if sign == '-':
            blacklist.add(subnet)
        else:
            whitelist.add(subnet)

    # Get the optimised blacklist and intersection
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)
    intersection = get_intersection(blacklist, whitelist)

    # Check if there is a contradiction
    if len(intersection) > 0:
        print(-1)
    else:
        # Print the length of the optimised blacklist
        print(len(optimized_blacklist))

        # Print the optimised blacklist
        for subnet in optimized_blacklist:
            print(subnet)

if __name__ == '__main__':
    main()


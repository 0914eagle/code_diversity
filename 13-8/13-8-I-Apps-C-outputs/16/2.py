
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

def get_ipv4_subnets(input_list):
    # Initialize the output list
    output_list = []

    # Iterate over the input list
    for subnet in input_list:
        # If the subnet is in CIDR format, convert it to IPv4 format
        if "/" in subnet:
            subnet = subnet.split("/")[0]

        # Add the subnet to the output list
        output_list.append(subnet)

    # Return the output list
    return output_list

def main():
    # Read the number of subnets from stdin
    n = int(input())

    # Read the subnets from stdin
    blacklist = get_ipv4_subnets(input().split())
    whitelist = get_ipv4_subnets(input().split())

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # If there is no IPv4 address that matches both the whitelist and the blacklist, print the length of the optimized blacklist and the subnets
    if len(optimized_blacklist) == 0:
        print(-1)
    else:
        print(len(optimized_blacklist))
        for subnet in optimized_blacklist:
            print(subnet)

if __name__ == '__main__':
    main()


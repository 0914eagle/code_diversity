
def get_optimized_blacklist(blacklist, whitelist):
    # Initialize the optimized blacklist with the blacklist
    optimized_blacklist = blacklist.copy()

    # Loop through the whitelist and remove any subnets that are also in the blacklist
    for subnet in whitelist:
        if subnet in optimized_blacklist:
            optimized_blacklist.remove(subnet)

    # Return the optimized blacklist
    return optimized_blacklist

def get_intersection(subnet1, subnet2):
    # Convert the subnets to integers
    subnet1_int = ip_to_int(subnet1)
    subnet2_int = ip_to_int(subnet2)

    # Get the intersection of the two subnets
    intersection = subnet1_int & subnet2_int

    # Convert the intersection back to a subnet
    intersection_subnet = int_to_ip(intersection)

    # Return the intersection subnet
    return intersection_subnet

def ip_to_int(ip):
    # Split the IP address into octets
    octets = ip.split(".")

    # Convert each octet to an integer
    octet1 = int(octets[0])
    octet2 = int(octets[1])
    octet3 = int(octets[2])
    octet4 = int(octets[3])

    # Calculate the total IP address as a 32-bit integer
    total_ip = octet1 * (2**24) + octet2 * (2**16) + octet3 * (2**8) + octet4

    # Return the total IP address
    return total_ip

def int_to_ip(total_ip):
    # Calculate the octet values
    octet4 = total_ip % 256
    octet3 = (total_ip // 256) % 256
    octet2 = (total_ip // 256 // 256) % 256
    octet1 = total_ip // 256 // 256 // 256

    # Convert the octet values to strings
    octet1_str = str(octet1)
    octet2_str = str(octet2)
    octet3_str = str(octet3)
    octet4_str = str(octet4)

    # Return the IP address as a string
    return octet1_str + "." + octet2_str + "." + octet3_str + "." + octet4_str

def main():
    # Get the number of subnets
    n = int(input())

    # Initialize the blacklist and whitelist
    blacklist = []
    whitelist = []

    # Loop through the subnets
    for i in range(n):
        # Get the current subnet
        subnet = input()

        # Check if the subnet is in the blacklist or whitelist
        if subnet.startswith("-"):
            blacklist.append(subnet[1:])
        elif subnet.startswith("+"):
            whitelist.append(subnet[1:])

    # Get the optimized blacklist
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)

    # Check if there is a contradiction
    if len(optimized_blacklist) == 0:
        print(-1)
    else:
        # Print the length of the optimized blacklist
        print(len(optimized_blacklist))

        # Loop through the optimized blacklist and print each subnet
        for subnet in optimized_blacklist:
            print(subnet)

if __name__ == '__main__':
    main()


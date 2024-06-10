
def get_optimized_blacklist(blacklist, whitelist):
    # Step 1: Initialize the optimized blacklist with the blacklist
    optimized_blacklist = set(blacklist)
    
    # Step 2: Add all whitelisted IP addresses to the optimized blacklist
    for ip in whitelist:
        optimized_blacklist.add(ip)
    
    # Step 3: Remove all IP addresses that are whitelisted but not blacklisted
    for ip in whitelist:
        if ip not in blacklist:
            optimized_blacklist.remove(ip)
    
    return optimized_blacklist

def get_subnets_from_blacklist(blacklist):
    subnets = set()
    for ip in blacklist:
        subnets.add(ip)
        subnets.add(ip + "/32")
    return subnets

def get_subnets_from_whitelist(whitelist):
    subnets = set()
    for ip in whitelist:
        subnets.add(ip)
        subnets.add(ip + "/32")
    return subnets

def get_intersection_of_subnets(subnets1, subnets2):
    intersection = set()
    for subnet in subnets1:
        if subnet in subnets2:
            intersection.add(subnet)
    return intersection

def get_difference_of_subnets(subnets1, subnets2):
    difference = set()
    for subnet in subnets1:
        if subnet not in subnets2:
            difference.add(subnet)
    return difference

def get_optimized_blacklist_from_intersection(intersection):
    optimized_blacklist = set()
    for subnet in intersection:
        optimized_blacklist.add(subnet)
        optimized_blacklist.add(subnet + "/32")
    return optimized_blacklist

def main():
    n = int(input())
    blacklist = set()
    whitelist = set()
    for i in range(n):
        line = input().split()
        if line[0] == "-":
            blacklist.add(line[1])
        else:
            whitelist.add(line[1])
    
    # Get the subnets from the blacklist and whitelist
    blacklist_subnets = get_subnets_from_blacklist(blacklist)
    whitelist_subnets = get_subnets_from_whitelist(whitelist)
    
    # Get the intersection of the blacklist and whitelist subnets
    intersection = get_intersection_of_subnets(blacklist_subnets, whitelist_subnets)
    
    # Get the difference of the blacklist and whitelist subnets
    difference = get_difference_of_subnets(blacklist_subnets, whitelist_subnets)
    
    # Get the optimized blacklist from the intersection
    optimized_blacklist = get_optimized_blacklist_from_intersection(intersection)
    
    # Add the difference to the optimized blacklist
    for subnet in difference:
        optimized_blacklist.add(subnet)
    
    print(-1)
    return optimized_blacklist

if __name__ == '__main__':
    main()


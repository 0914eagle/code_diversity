
def get_optimized_blacklist(blacklist, whitelist):
    # Step 1: Initialize the optimized blacklist as an empty set
    optimized_blacklist = set()
    
    # Step 2: Iterate over the blacklist and whitelist and add the subnets to the optimized blacklist
    for subnet in blacklist:
        optimized_blacklist.add(subnet)
    for subnet in whitelist:
        optimized_blacklist.discard(subnet)
    
    # Step 3: Return the optimized blacklist
    return optimized_blacklist

def main():
    # Step 1: Read the number of subnets from stdin
    n = int(input())
    
    # Step 2: Read the subnets from stdin and store them in a set
    blacklist = set()
    whitelist = set()
    for _ in range(n):
        sign, subnet = input().split()
        if sign == '-':
            blacklist.add(subnet)
        elif sign == '+':
            whitelist.add(subnet)
    
    # Step 3: Call the get_optimized_blacklist function and store the result in a variable
    optimized_blacklist = get_optimized_blacklist(blacklist, whitelist)
    
    # Step 4: Print the length of the optimized blacklist and the subnets in the optimized blacklist
    print(len(optimized_blacklist))
    for subnet in optimized_blacklist:
        print(subnet)

if __name__ == '__main__':
    main()


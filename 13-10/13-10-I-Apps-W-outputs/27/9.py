
def get_boring_pairs(n, paths):
    # Initialize a dictionary to store the pairs of planets and their curiosity values
    pairs = {}
    for path in paths:
        pair = (path[0], path[1])
        pairs[pair] = path[2]
    
    # Initialize a set to store the destroyed paths
    destroyed = set()
    
    # Initialize a dictionary to store the number of boring pairs after each destruction
    boring_pairs = {}
    
    # Loop through each path and check if it is boring
    for path in paths:
        pair = (path[0], path[1])
        if pair not in destroyed:
            # Check if the pair is boring
            if xor_curiosity(path[2], destroyed) == 0:
                # Add the pair to the dictionary of boring pairs
                boring_pairs[pair] = boring_pairs.get(pair, 0) + 1
    
    return boring_pairs

def xor_curiosity(curiosity, destroyed):
    # Initialize a variable to store the XOR of the curiosity values
    xor = 0
    
    # Loop through each path and check if it is destroyed
    for path in destroyed:
        # XOR the curiosity value with the current XOR value
        xor ^= path[2]
    
    # Return the XOR of the curiosity values
    return xor

def main():
    # Read the input
    n = int(input())
    paths = []
    for i in range(n - 1):
        paths.append(list(map(int, input().split())))
    destruction_order = list(map(int, input().split()))
    
    # Get the boring pairs before any destructions
    boring_pairs = get_boring_pairs(n, paths)
    
    # Loop through each destruction and get the number of boring pairs after each destruction
    for i in range(1, n):
        print(len(get_boring_pairs(n, paths[:i] + paths[i:])))

if __name__ == '__main__':
    main()


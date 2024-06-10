
def get_splitters(a, b, c, d):
    # Initialize the number of splitters to 0
    n = 0
    
    # Initialize the list of splitters
    splitters = []
    
    # While there are still boxes to be distributed
    while c > 0 or d > 0:
        # If the current splitter has not been used yet
        if n not in splitters:
            # Add the current splitter to the list of splitters
            splitters.append(n)
            # Decrement the number of boxes to be distributed by the ratio of the current splitter
            c -= a / (a + b)
            d -= b / (a + b)
            # Increment the number of splitters
            n += 1
    
    # If there are still boxes to be distributed
    if c > 0 or d > 0:
        # Return -1 to indicate that it is not possible to distribute the boxes with the given constraints
        return -1
    
    # Otherwise, return the list of splitters
    return splitters

def get_network(a, b, c, d):
    # Get the list of splitters
    splitters = get_splitters(a, b, c, d)
    
    # If the list of splitters is -1, return -1 to indicate that it is not possible to distribute the boxes with the given constraints
    if splitters == -1:
        return -1
    
    # Initialize the network with the global input belt and the first global output belt
    network = [0, -2]
    
    # For each splitter in the list of splitters
    for i in range(1, len(splitters)):
        # Get the index of the splitter connected to the left output
        l = splitters[i - 1]
        # Get the index of the splitter connected to the right output
        r = splitters[i]
        # Add the splitter to the network
        network.append(l)
        network.append(r)
    
    # Return the network
    return network

def main():
    # Read the input
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # Get the network
    network = get_network(a, b, c, d)
    
    # If the network is -1, print -1
    if network == -1:
        print(-1)
    # Otherwise, print the network
    else:
        print(len(network))
        for i in network:
            print(i, end=" ")

if __name__ == '__main__':
    main()


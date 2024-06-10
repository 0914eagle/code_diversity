
def create_splitter_network(a, b, c, d):
    # Initialize the network with a single input belt and two output belts
    network = [(0, 1, 2)]
    splitters = []
    
    # Loop until the desired splitter ratio is reached
    while True:
        # Find the splitter with the lowest index that can be used to distribute the input
        current_splitter = min(network, key=lambda x: x[0])
        
        # If the current splitter has a ratio that matches the desired ratio, return the network
        if current_splitter[1] == c and current_splitter[2] == d:
            return network
        
        # Otherwise, create a new splitter with the desired ratio and add it to the network
        new_splitter = (len(network), c, d)
        network.append(new_splitter)
        splitters.append(new_splitter)
        
        # Connect the new splitter to the input and output belts
        network.append((new_splitter[0], current_splitter[1], new_splitter[1]))
        network.append((new_splitter[0], new_splitter[2], current_splitter[2]))
        
        # Update the network with the new splitter
        network.remove(current_splitter)
        network.append(new_splitter)
    
    # Return the network with the desired splitter ratio
    return network

def main():
    a, b, c, d = map(int, input().split())
    network = create_splitter_network(a, b, c, d)
    print(len(network))
    for splitter in network:
        print(splitter[0], splitter[1], splitter[2])

if __name__ == '__main__':
    main()


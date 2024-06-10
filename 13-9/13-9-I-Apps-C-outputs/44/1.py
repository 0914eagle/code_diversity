
def get_splitter_network(a, b, c, d):
    # Initialize the network with a single input and two output belts
    network = {
        "input": [],
        "output1": [],
        "output2": []
    }
    
    # Initialize the number of splitters used
    num_splitters = 0
    
    # Initialize the indices of the splitters
    indices = [-1, -2]
    
    # Loop until the global input is distributed in the desired ratio
    while True:
        # Check if the global input is already distributed in the desired ratio
        if network["input"][0] == c / (c + d) and network["input"][1] == d / (c + d):
            break
        
        # Add a new splitter to the network
        network[f"splitter{num_splitters}"] = []
        network["input"].append(a / (a + b))
        network["input"].append(b / (a + b))
        indices.append(num_splitters)
        num_splitters += 1
        
        # Connect the new splitter to the output belts
        network[f"splitter{num_splitters - 1}"].append(indices[0])
        network[f"splitter{num_splitters - 1}"].append(indices[1])
        
        # Check if the number of splitters used exceeds the maximum allowed
        if num_splitters > 200:
            return None
    
    # Return the network and the number of splitters used
    return network, num_splitters

def get_splitter_configuration(a, b, c, d):
    # Get the splitter network
    network, num_splitters = get_splitter_network(a, b, c, d)
    
    # Initialize the configuration of the splitters
    configuration = []
    
    # Loop over the splitters in the network
    for i in range(num_splitters):
        # Get the indices of the splitter's outputs
        output1, output2 = network[f"splitter{i}"]
        
        # Check if the splitter is connected to the output belts
        if output1 == -1:
            output1 = "output1"
        if output2 == -2:
            output2 = "output2"
        
        # Add the splitter's configuration to the configuration list
        configuration.append([i, output1, output2])
    
    # Return the configuration of the splitters
    return configuration

if __name__ == '__main__':
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    configuration = get_splitter_configuration(a, b, c, d)
    print(len(configuration))
    for i, output1, output2 in configuration:
        print(i, output1, output2)



def get_splitter_network(a, b, c, d):
    # Initialize the network with a single input belt and two output belts
    network = {
        "input": [],
        "output1": [],
        "output2": []
    }
    
    # Calculate the ratio of boxes sent to each output
    output1_ratio = c / (c + d)
    output2_ratio = d / (c + d)
    
    # Initialize the number of splitters used
    num_splitters = 0
    
    # Loop until the global input is distributed evenly between the two outputs
    while True:
        # Calculate the number of boxes sent to each output based on the current network configuration
        output1_boxes = len(network["output1"])
        output2_boxes = len(network["output2"])
        
        # If the number of boxes on both outputs is equal, break the loop
        if output1_boxes == output2_boxes:
            break
        
        # If the number of boxes on the first output is less than the number of boxes on the second output, add a splitter to the first output
        if output1_boxes < output2_boxes:
            # Add a new splitter to the network
            network[num_splitters] = {
                "input": network["output1"],
                "output1": [],
                "output2": []
            }
            
            # Update the output belts of the previous splitter
            network[num_splitters - 1]["output1"] = network[num_splitters]["input"]
            
            # Update the input belt of the new splitter
            network[num_splitters]["input"] = network["input"]
            
            # Update the number of splitters used
            num_splitters += 1
            
        # If the number of boxes on the first output is greater than the number of boxes on the second output, add a splitter to the second output
        else:
            # Add a new splitter to the network
            network[num_splitters] = {
                "input": network["output2"],
                "output1": [],
                "output2": []
            }
            
            # Update the output belts of the previous splitter
            network[num_splitters - 1]["output2"] = network[num_splitters]["input"]
            
            # Update the input belt of the new splitter
            network[num_splitters]["input"] = network["input"]
            
            # Update the number of splitters used
            num_splitters += 1
    
    # Return the number of splitters used and the connection details
    return num_splitters, network

def main():
    # Read the input ratios
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # Get the splitter network
    num_splitters, network = get_splitter_network(a, b, c, d)
    
    # Print the number of splitters used
    print(num_splitters)
    
    # Print the connection details
    for i in range(num_splitters):
        # Get the output belts of the current splitter
        output1 = network[i]["output1"]
        output2 = network[i]["output2"]
        
        # If the current splitter is the first splitter, the input belt is the global input
        if i == 0:
            input_belts = "input"
        # If the current splitter is not the first splitter, the input belt is the output of the previous splitter
        else:
            input_belts = network[i - 1]["output1"]
        
        # Print the connection details
        print(input_belts, output1, output2)

if __name__ == '__main__':
    main()


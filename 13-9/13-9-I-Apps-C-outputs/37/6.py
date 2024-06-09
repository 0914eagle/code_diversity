
def solve(n, data):
    # Initialize a dictionary to store the input values
    inputs = {}
    # Initialize a dictionary to store the output values
    outputs = {}
    # Loop through the data and populate the input and output dictionaries
    for line in data:
        tokens = line.split()
        if tokens[0] == "IN":
            inputs[int(tokens[1])] = int(tokens[2])
        else:
            outputs[int(tokens[1])] = int(tokens[2])
    
    # Function to evaluate the output for a given input
    def evaluate(input_values):
        # Loop through the inputs and populate the dictionary with their values
        for i in range(1, n+1):
            if i in inputs:
                inputs[i] = input_values[i-1]
        
        # Evaluate the output for the given input
        output = outputs[1]
        for i in range(2, n+1):
            if outputs[i] == 2:
                output = inputs[outputs[i]] ^ inputs[outputs[i+1]]
            elif outputs[i] == 3:
                output = inputs[outputs[i]] | inputs[outputs[i+1]]
            elif outputs[i] == 4:
                output = inputs[outputs[i]] & inputs[outputs[i+1]]
            else:
                output = ~inputs[outputs[i]]
        
        return output
    
    # Return the output for each input in the ascending order of their vertex indices
    return ''.join(str(evaluate(input_values)) for input_values in inputs.values())


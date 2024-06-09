
def solve(n, edges):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i+1] = 0

    # Initialize a dictionary to store the values of the outputs
    outputs = {}
    for i in range(n):
        outputs[i+1] = 0

    # Iterate through the edges and update the values of the outputs
    for edge in edges:
        if edge[0] == 1:
            # Edge is an input, so set the output to the input value
            outputs[edge[1]] = inputs[edge[1]]
        else:
            # Edge is a logical element, so calculate the output value
            if edge[0] == "AND":
                outputs[edge[1]] = inputs[edge[2]] & inputs[edge[3]]
            elif edge[0] == "OR":
                outputs[edge[1]] = inputs[edge[2]] | inputs[edge[3]]
            elif edge[0] == "XOR":
                outputs[edge[1]] = inputs[edge[2]] ^ inputs[edge[3]]
            elif edge[0] == "NOT":
                outputs[edge[1]] = ~inputs[edge[2]]

    # Return the output values as a string
    return "".join(str(outputs[i+1]) for i in range(n))


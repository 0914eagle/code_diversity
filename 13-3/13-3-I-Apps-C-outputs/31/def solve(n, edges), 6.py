
def solve(n, edges):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i] = 0

    # Initialize a dictionary to store the values of the outputs
    outputs = {}
    for i in range(n):
        outputs[i] = 0

    # Iterate through the edges and update the values of the outputs
    for edge in edges:
        if edge[0] == 0:
            # Edge is an input, so set the output to the input value
            outputs[edge[1]] = inputs[edge[1]]
        else:
            # Edge is a logical element, so compute the output value
            if edge[0] == 1:
                # AND element
                outputs[edge[1]] = inputs[edge[2]] & inputs[edge[3]]
            elif edge[0] == 2:
                # OR element
                outputs[edge[1]] = inputs[edge[2]] | inputs[edge[3]]
            elif edge[0] == 3:
                # XOR element
                outputs[edge[1]] = inputs[edge[2]] ^ inputs[edge[3]]
            elif edge[0] == 4:
                # NOT element
                outputs[edge[1]] = ~inputs[edge[2]]

    # Return the output values as a string of '0' and '1' characters
    return ''.join(str(int(outputs[i])) for i in range(1, n))


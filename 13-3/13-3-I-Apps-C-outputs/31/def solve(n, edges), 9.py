
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
            # If the edge is from the root (vertex 1) to a leaf (input), set the value of the output to the value of the input
            outputs[edge[1]] = inputs[edge[1]]
        else:
            # If the edge is from a logical element to another logical element or to the root, calculate the value of the output based on the function of the logical element
            if edge[0] == 2:
                # AND function
                outputs[edge[1]] = inputs[edge[1]] and inputs[edge[2]]
            elif edge[0] == 3:
                # OR function
                outputs[edge[1]] = inputs[edge[1]] or inputs[edge[2]]
            elif edge[0] == 4:
                # XOR function
                outputs[edge[1]] = inputs[edge[1]] ^ inputs[edge[2]]
            elif edge[0] == 5:
                # NOT function
                outputs[edge[1]] = not inputs[edge[1]]

    # Return the values of the outputs in the ascending order of their vertex indices
    return ''.join(str(outputs[i+1]) for i in range(n))


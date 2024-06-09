
def solve(n, graph):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i+1] = 0

    # Initialize a dictionary to store the values of the outputs
    outputs = {}
    for i in range(n):
        outputs[i+1] = 0

    # Iterate through the graph and calculate the values of the outputs
    for i in range(n):
        vertex = graph[i]
        if vertex[0] == "IN":
            # If the vertex is an input, set its value to the corresponding input value
            outputs[i+1] = inputs[vertex[1]]
        else:
            # If the vertex is a logical element, calculate its value based on the values of its inputs
            if vertex[0] == "AND":
                outputs[i+1] = inputs[vertex[1]] & inputs[vertex[2]]
            elif vertex[0] == "OR":
                outputs[i+1] = inputs[vertex[1]] | inputs[vertex[2]]
            elif vertex[0] == "XOR":
                outputs[i+1] = inputs[vertex[1]] ^ inputs[vertex[2]]
            elif vertex[0] == "NOT":
                outputs[i+1] = ~inputs[vertex[1]]

    # Return the values of the outputs as a string of '0's and '1's
    return "".join(str(outputs[i]) for i in range(1, n+1))



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
            # If the vertex is an input, set its value to the given input
            inputs[i+1] = vertex[1]
        else:
            # If the vertex is a logical element, calculate its value based on the values of its inputs
            if vertex[0] == "AND":
                inputs[i+1] = inputs[vertex[1]] & inputs[vertex[2]]
            elif vertex[0] == "OR":
                inputs[i+1] = inputs[vertex[1]] | inputs[vertex[2]]
            elif vertex[0] == "XOR":
                inputs[i+1] = inputs[vertex[1]] ^ inputs[vertex[2]]
            elif vertex[0] == "NOT":
                inputs[i+1] = ~inputs[vertex[1]]
            outputs[i+1] = inputs[i+1]

    # Return the values of the outputs
    return "".join(str(output) for output in outputs.values())


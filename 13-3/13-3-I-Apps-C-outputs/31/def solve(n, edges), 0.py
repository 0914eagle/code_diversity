
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
            # Edge from the root to an input vertex
            outputs[edge[1]] = inputs[edge[1]]
        else:
            # Edge from a logical element to an input vertex
            if edge[2] == "AND":
                outputs[edge[1]] = inputs[edge[3]] & inputs[edge[4]]
            elif edge[2] == "OR":
                outputs[edge[1]] = inputs[edge[3]] | inputs[edge[4]]
            elif edge[2] == "XOR":
                outputs[edge[1]] = inputs[edge[3]] ^ inputs[edge[4]]
            elif edge[2] == "NOT":
                outputs[edge[1]] = ~inputs[edge[3]]

    # Return the values of the outputs
    return "".join(str(outputs[i]) for i in range(1, n+1))


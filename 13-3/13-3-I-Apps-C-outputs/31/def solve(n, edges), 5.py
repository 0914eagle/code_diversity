
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
            # Input vertex, so set the value to the given input
            outputs[edge[1]] = inputs[edge[1]]
        else:
            # Logical vertex, so calculate the value based on the inputs
            if edge[0] == 2:
                # AND vertex
                outputs[edge[1]] = inputs[edge[2]] & inputs[edge[3]]
            elif edge[0] == 3:
                # OR vertex
                outputs[edge[1]] = inputs[edge[2]] | inputs[edge[3]]
            elif edge[0] == 4:
                # XOR vertex
                outputs[edge[1]] = inputs[edge[2]] ^ inputs[edge[3]]
            elif edge[0] == 5:
                # NOT vertex
                outputs[edge[1]] = ~inputs[edge[2]]

    # Return the values of the outputs
    return "".join(str(outputs[i]) for i in range(1, n+1))


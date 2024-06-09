
def solve(n, edges):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i+1] = 0
    
    # Initialize a dictionary to store the values of the outputs
    outputs = {}
    for i in range(n):
        outputs[i+1] = 0
    
    # Iterate through the edges and perform the logical operations
    for edge in edges:
        if edge[0] == "AND":
            outputs[edge[1]] = inputs[edge[2]] & inputs[edge[3]]
        elif edge[0] == "OR":
            outputs[edge[1]] = inputs[edge[2]] | inputs[edge[3]]
        elif edge[0] == "XOR":
            outputs[edge[1]] = inputs[edge[2]] ^ inputs[edge[3]]
        elif edge[0] == "NOT":
            outputs[edge[1]] = ~inputs[edge[2]]
        elif edge[0] == "IN":
            outputs[edge[1]] = inputs[edge[2]]
    
    # Return the values of the outputs
    return "".join(str(outputs[i]) for i in range(1, n+1))


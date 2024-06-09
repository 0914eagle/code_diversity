
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
        if graph[i][0] == "IN":
            # If the vertex is an input, set its value to the given input value
            outputs[i+1] = inputs[i+1]
        elif graph[i][0] == "AND":
            # If the vertex is an AND gate, calculate the output value based on the inputs
            outputs[i+1] = inputs[graph[i][1]] & inputs[graph[i][2]]
        elif graph[i][0] == "OR":
            # If the vertex is an OR gate, calculate the output value based on the inputs
            outputs[i+1] = inputs[graph[i][1]] | inputs[graph[i][2]]
        elif graph[i][0] == "XOR":
            # If the vertex is an XOR gate, calculate the output value based on the inputs
            outputs[i+1] = inputs[graph[i][1]] ^ inputs[graph[i][2]]
        elif graph[i][0] == "NOT":
            # If the vertex is a NOT gate, calculate the output value based on the input
            outputs[i+1] = ~inputs[graph[i][1]] & 1

    # Return the values of the outputs
    return "".join(str(int(outputs[i+1])) for i in range(n))


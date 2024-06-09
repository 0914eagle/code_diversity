
def solve(n, scheme):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i+1] = 0

    # Initialize a dictionary to store the values of the outputs
    outputs = {}
    for i in range(n):
        outputs[i+1] = 0

    # Iterate through the scheme and calculate the values of the outputs
    for vertex in scheme:
        if vertex[0] == "AND":
            inputs[vertex[1]] = inputs[vertex[1]] & inputs[vertex[2]]
        elif vertex[0] == "OR":
            inputs[vertex[1]] = inputs[vertex[1]] | inputs[vertex[2]]
        elif vertex[0] == "XOR":
            inputs[vertex[1]] = inputs[vertex[1]] ^ inputs[vertex[2]]
        elif vertex[0] == "NOT":
            inputs[vertex[1]] = ~inputs[vertex[1]]
        else:
            inputs[vertex[0]] = vertex[1]

    # Return the values of the outputs
    return "".join(str(outputs[i+1]) for i in range(n))



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
            outputs[vertex[1]] = inputs[vertex[2]] & inputs[vertex[3]]
        elif vertex[0] == "OR":
            outputs[vertex[1]] = inputs[vertex[2]] | inputs[vertex[3]]
        elif vertex[0] == "XOR":
            outputs[vertex[1]] = inputs[vertex[2]] ^ inputs[vertex[3]]
        elif vertex[0] == "NOT":
            outputs[vertex[1]] = ~inputs[vertex[2]]
        elif vertex[0] == "IN":
            inputs[vertex[1]] = vertex[2]

    # Return the values of the outputs
    return "".join(str(output) for output in outputs.values())


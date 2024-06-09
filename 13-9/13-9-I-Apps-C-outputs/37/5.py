
def solve(n, vertices):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for vertex in vertices:
        if vertex[0] == "IN":
            inputs[vertex[1]] = vertex[2]

    # Initialize a dictionary to store the values of the outputs
    outputs = {}

    # Iterate through the vertices and calculate the values of the outputs
    for vertex in vertices:
        if vertex[0] == "AND":
            inputs1 = inputs[vertex[1]]
            inputs2 = inputs[vertex[2]]
            outputs[vertex[3]] = str(int(inputs1) & int(inputs2))
        elif vertex[0] == "OR":
            inputs1 = inputs[vertex[1]]
            inputs2 = inputs[vertex[2]]
            outputs[vertex[3]] = str(int(inputs1) | int(inputs2))
        elif vertex[0] == "XOR":
            inputs1 = inputs[vertex[1]]
            inputs2 = inputs[vertex[2]]
            outputs[vertex[3]] = str(int(inputs1) ^ int(inputs2))
        elif vertex[0] == "NOT":
            inputs1 = inputs[vertex[1]]
            outputs[vertex[2]] = str(int(not int(inputs1)))

    # Return the values of the outputs in the order of the vertices
    return "".join(outputs[i] for i in range(1, n + 1))


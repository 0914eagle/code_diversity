
def get_output(n, logical_scheme):
    # Initialize a dictionary to store the values of the inputs
    inputs = {}
    for i in range(n):
        inputs[i+1] = 0

    # Initialize a dictionary to store the values of the logical elements
    elements = {}
    for i in range(n, 2*n-1):
        elements[i+1] = 0

    # Process the logical scheme
    for i in range(n):
        vertex_type = logical_scheme[i][0]
        if vertex_type == "AND":
            elements[i+1] = inputs[logical_scheme[i][1]] & inputs[logical_scheme[i][2]]
        elif vertex_type == "OR":
            elements[i+1] = inputs[logical_scheme[i][1]] | inputs[logical_scheme[i][2]]
        elif vertex_type == "XOR":
            elements[i+1] = inputs[logical_scheme[i][1]] ^ inputs[logical_scheme[i][2]]
        elif vertex_type == "NOT":
            elements[i+1] = ~inputs[logical_scheme[i][1]]
        elif vertex_type == "IN":
            inputs[i+1] = logical_scheme[i][1]

    # Return the output values
    output = ""
    for i in range(n):
        output += str(elements[i+1])
    return output


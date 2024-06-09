
def solve(n, logical_scheme):
    # Initialize a dictionary to store the values of the inputs
    input_values = {}
    # Initialize a dictionary to store the values of the outputs
    output_values = {}
    # Loop through each vertex in the graph
    for vertex in logical_scheme:
        # If the vertex is an input, store its value
        if vertex[0] == "IN":
            input_values[vertex[1]] = vertex[2]
        # If the vertex is not an input, calculate its value based on the values of its inputs
        else:
            # Get the indices of the input vertices
            input_indices = vertex[1:]
            # Get the values of the input vertices
            input_values_list = [input_values[index] for index in input_indices]
            # Calculate the value of the vertex based on the input values
            if vertex[0] == "AND":
                output_values[vertex[1]] = int(all(input_values_list))
            elif vertex[0] == "OR":
                output_values[vertex[1]] = int(any(input_values_list))
            elif vertex[0] == "XOR":
                output_values[vertex[1]] = int(sum(input_values_list) % 2)
            elif vertex[0] == "NOT":
                output_values[vertex[1]] = int(not input_values_list[0])
    # Return the values of the outputs
    return "".join(str(output_values[i]) for i in range(1, n+1))


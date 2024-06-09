
def solve(n, vertices):
    # Initialize a dictionary to store the values of the inputs
    input_values = {}
    # Initialize a dictionary to store the values of the outputs
    output_values = {}
    # Iterate over the vertices
    for vertex in vertices:
        # If the vertex is an input, store its value
        if vertex[0] == "IN":
            input_values[vertex[1]] = vertex[2]
        # If the vertex is not an input, calculate its value based on its type and the values of its inputs
        else:
            # Get the type of the vertex
            vertex_type = vertex[0]
            # Get the indices of the input vertices
            input_indices = vertex[1:]
            # Initialize the value of the vertex to 0
            value = 0
            # Iterate over the input indices
            for input_index in input_indices:
                # If the input index is not in the dictionary, it means it is an input vertex that has not been processed yet
                if input_index not in input_values:
                    # In this case, break the loop and move on to the next vertex
                    break
                # If the input index is in the dictionary, get its value
                input_value = input_values[input_index]
                # Depending on the vertex type, calculate the value of the vertex
                if vertex_type == "AND":
                    value &= input_value
                elif vertex_type == "OR":
                    value |= input_value
                elif vertex_type == "XOR":
                    value ^= input_value
                elif vertex_type == "NOT":
                    value = ~input_value
            # If the vertex is an output vertex, store its value
            if vertex[1] == 1:
                output_values[vertex[1]] = value
    # Return the values of the outputs
    return "".join(str(output_values[i]) for i in sorted(output_values))


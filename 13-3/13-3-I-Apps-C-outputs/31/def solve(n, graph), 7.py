
def solve(n, graph):
    # Initialize the output string
    output = ""
    
    # Iterate over each input vertex
    for i in range(2, n):
        # Get the type of the current vertex
        vertex_type = graph[i][0]
        
        # If the current vertex is an input, append its value to the output string
        if vertex_type == "IN":
            output += str(graph[i][1])
        # If the current vertex is a logical element, calculate its output based on its inputs
        else:
            # Get the indices of the input vertices
            input_indices = graph[i][1:]
            
            # Initialize the output of the current vertex to 0
            output_vertex = 0
            
            # Iterate over each input vertex
            for j in input_indices:
                # If the current input vertex is an input, get its value
                if graph[j][0] == "IN":
                    input_value = graph[j][1]
                # If the current input vertex is a logical element, get its output
                else:
                    input_value = output[j-1]
                
                # Update the output of the current vertex based on the input value and the logical element type
                if vertex_type == "AND":
                    output_vertex &= input_value
                elif vertex_type == "OR":
                    output_vertex |= input_value
                elif vertex_type == "XOR":
                    output_vertex ^= input_value
                elif vertex_type == "NOT":
                    output_vertex = 1 - output_vertex
            
            # Append the output of the current vertex to the output string
            output += str(output_vertex)
    
    return output


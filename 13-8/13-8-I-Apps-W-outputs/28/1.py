
def get_minimal_bdd_size(n, function_values):
    # Initialize a dictionary to store the BDD nodes
    nodes = {}
    
    # Initialize the root node with function value 1
    root = 1
    nodes[root] = {}
    
    # Iterate over the function values
    for i in range(len(function_values)):
        # Get the current function value
        current_value = function_values[i]
        
        # If the current value is 0, skip this iteration
        if current_value == 0:
            continue
        
        # Get the current node
        current_node = root
        
        # Iterate over the bits of the current value
        for j in range(n):
            # Get the current bit
            current_bit = (current_value >> j) & 1
            
            # If the current bit is 0, skip this iteration
            if current_bit == 0:
                continue
            
            # If the current node does not have a child node for the current bit, create one
            if j not in nodes[current_node]:
                nodes[current_node][j] = len(nodes)
                nodes[nodes[current_node][j]] = {}
            
            # Set the current node to the child node for the current bit
            current_node = nodes[current_node][j]
    
    # Return the number of vertices in the BDD
    return len(nodes)


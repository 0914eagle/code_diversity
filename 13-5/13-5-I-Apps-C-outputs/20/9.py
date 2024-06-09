
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    
    # Iterate until the total time spent is less than or equal to t
    while t > 0:
        # Get the current node
        current_node = data_nodes[-1]
        
        # Generate the next node based on the given rules
        next_node = (a_x * current_node[0] + b_x, a_y * current_node[1] + b_y)
        
        # If the next node is not already in the list, add it
        if next_node not in data_nodes:
            data_nodes.append(next_node)
        
        # Decrement the time by 1
        t -= 1
    
    # Return the number of data nodes collected
    return len(data_nodes)


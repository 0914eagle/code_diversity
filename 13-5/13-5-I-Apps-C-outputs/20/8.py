
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    
    # Calculate the coordinates of the next data node
    next_x = a_x * x0 + b_x
    next_y = a_y * y0 + b_y
    
    # Add the next data node to the list
    data_nodes.append((next_x, next_y))
    
    # Continue calculating the coordinates of the next data node until the list is empty
    while len(data_nodes) > 0:
        # Pop the last node from the list
        node = data_nodes.pop()
        
        # Calculate the coordinates of the next data node
        next_x = a_x * node[0] + b_x
        next_y = a_y * node[1] + b_y
        
        # Add the next data node to the list
        data_nodes.append((next_x, next_y))
    
    # Initialize a variable to store the maximum number of data nodes collected
    max_nodes = 0
    
    # Initialize a variable to store the current number of data nodes collected
    current_nodes = 0
    
    # Initialize a variable to store the current time
    current_time = 0
    
    # Iterate through the data nodes
    for node in data_nodes:
        # Calculate the distance between the current node and the starting point
        distance = abs(node[0] - x_s) + abs(node[1] - y_s)
        
        # If the current node is within the time limit, add it to the list of collected nodes
        if current_time + distance <= t:
            current_nodes += 1
            current_time += distance
        
        # If the current number of collected nodes is greater than the maximum number of collected nodes, update the maximum number of collected nodes
        if current_nodes > max_nodes:
            max_nodes = current_nodes
    
    # Return the maximum number of collected nodes
    return max_nodes


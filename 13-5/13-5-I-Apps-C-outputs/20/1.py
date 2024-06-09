
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    
    # Calculate the coordinates of the remaining data nodes
    for i in range(1, 1000000):
        x = a_x * data_nodes[i-1][0] + b_x
        y = a_y * data_nodes[i-1][1] + b_y
        data_nodes.append((x, y))
    
    # Initialize a set to store the collected data nodes
    collected_nodes = set()
    
    # Initialize variables to store the current coordinate and time
    current_x = x_s
    current_y = y_s
    time = 0
    
    # Loop through the data nodes and calculate the maximum number of nodes that can be collected within t seconds
    max_nodes = 0
    for node in data_nodes:
        # Calculate the distance between the current coordinate and the current data node
        distance = abs(current_x - node[0]) + abs(current_y - node[1])
        
        # If the distance is less than or equal to t, add the data node to the collected nodes set and update the current coordinate and time
        if distance <= t:
            collected_nodes.add(node)
            current_x = node[0]
            current_y = node[1]
            time += distance
        
        # If the time exceeds t, break the loop
        if time > t:
            break
    
    # Return the maximum number of collected nodes
    return len(collected_nodes)


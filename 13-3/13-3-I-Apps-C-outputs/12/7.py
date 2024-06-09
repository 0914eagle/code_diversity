
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    
    # Initialize a set to store the coordinates of the visited nodes
    visited = set()
    
    # Initialize a variable to store the maximum number of data nodes collected
    max_data_nodes = 0
    
    # Loop through the coordinates of the data nodes
    for i in range(1, 1000000):
        # Calculate the coordinates of the next data node
        x = a_x * data_nodes[-1][0] + b_x
        y = a_y * data_nodes[-1][1] + b_y
        
        # If the next data node is not already visited, add it to the list of data nodes
        if (x, y) not in visited:
            data_nodes.append((x, y))
            visited.add((x, y))
        
        # If the current node is the starting node, break the loop
        if (x, y) == (x_s, y_s):
            break
    
    # Loop through the data nodes
    for i in range(len(data_nodes)):
        # Calculate the distance between the current node and the starting node
        distance = abs(data_nodes[i][0] - x_s) + abs(data_nodes[i][1] - y_s)
        
        # If the distance is less than or equal to the available time, add the current node to the list of collected nodes
        if distance <= t:
            max_data_nodes += 1
    
    return max_data_nodes


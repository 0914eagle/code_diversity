
def solve(x0, y0, a_x, a_y, b_x, b_y, x_s, y_s, t):
    # Initialize a list to store the coordinates of the data nodes
    data_nodes = [(x0, y0)]
    # Initialize a set to store the visited nodes
    visited = set()
    # Initialize a variable to store the maximum number of data nodes collected
    max_data_nodes = 0
    # Initialize a variable to store the current node
    current_node = (x_s, y_s)
    # Initialize a variable to store the time remaining
    time_remaining = t
    # Loop until the time remaining is zero or the current node is the starting node
    while time_remaining > 0 and current_node != (x0, y0):
        # Get the coordinates of the next node
        next_node = (a_x * current_node[0] + b_x, a_y * current_node[1] + b_y)
        # If the next node is not visited, add it to the list of data nodes and mark it as visited
        if next_node not in visited:
            data_nodes.append(next_node)
            visited.add(next_node)
        # Move to the next node and decrease the time remaining
        current_node = next_node
        time_remaining -= 1
    # Return the maximum number of data nodes collected
    return len(data_nodes)


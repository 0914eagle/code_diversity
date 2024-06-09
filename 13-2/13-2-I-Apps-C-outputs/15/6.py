
import math

def get_least_turning(nodes, edges):
    # Initialize variables
    turning = 0
    visited = set()
    current_node = 0
    previous_node = None

    # Loop through the edges
    for edge in edges:
        # If the current node has not been visited before, add it to the visited set
        if current_node not in visited:
            visited.add(current_node)
        # If the previous node is not None, calculate the turning required for this edge
        if previous_node is not None:
            turning += get_turning(nodes[current_node], nodes[previous_node])
        # Update the previous node and current node
        previous_node = current_node
        current_node = edge

    # Calculate the turning required for the final edge
    turning += get_turning(nodes[current_node], nodes[previous_node])

    return turning

def get_turning(node1, node2):
    # Calculate the angle between the two nodes
    angle = math.atan2(node2[1] - node1[1], node2[0] - node1[0])
    # Convert the angle to radians
    turning = math.radians(angle)
    return turning

# Test the function with the sample input
nodes = [(0, 0), (0, 1), (1, 0)]
edges = [(0, 1), (0, 2), (1, 2)]
print(get_least_turning(nodes, edges))

# 6.283185


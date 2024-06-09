
import math

def f1(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    visited_edges = set()

    # Loop through all nodes
    for i in range(N):
        # Get the edges connected to the current node
        edges_connected_to_current_node = [edge for edge in edges if edge[0] == current_node or edge[1] == current_node]

        # If the current node has not been visited before, add it to the visited nodes set
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)

        # If the current node has not been visited before, add it to the visited edges set
        if (current_node, edges_connected_to_current_node[0][1]) not in visited_edges:
            visited_edges.add((current_node, edges_connected_to_current_node[0][1]))

        # Calculate the turning required for the current node
        turning_required += calculate_turning_required(current_node, edges_connected_to_current_node)

        # Set the current node to the next node
        current_node = edges_connected_to_current_node[0][1]

    # Return the total turning required
    return turning_required

def calculate_turning_required(current_node, edges_connected_to_current_node):
    # Initialize variables
    turning_required = 0
    next_node = edges_connected_to_current_node[0][1]

    # If the current node has only one edge connected to it, add the turning required for the edge
    if len(edges_connected_to_current_node) == 1:
        turning_required += calculate_turning_required_for_edge(current_node, next_node)

    # If the current node has two edges connected to it, add the turning required for both edges
    elif len(edges_connected_to_current_node) == 2:
        turning_required += calculate_turning_required_for_edge(current_node, next_node)
        turning_required += calculate_turning_required_for_edge(current_node, edges_connected_to_current_node[1][1])

    # Return the total turning required
    return turning_required

def calculate_turning_required_for_edge(current_node, next_node):
    # Initialize variables
    turning_required = 0
    current_node_x, current_node_y = nodes[current_node]
    next_node_x, next_node_y = nodes[next_node]

    # Calculate the turning required for the edge
    turning_required = math.atan2(next_node_y - current_node_y, next_node_x - current_node_x)

    # Return the turning required
    return turning_required

def f2(...):
    # TODO: Implement this function
    pass

if __name__ == '__main__':
    # Test case 1:
    N = 3
    M = 3
    nodes = [(0, 0), (0, 1), (1, 0)]
    edges = [(0, 1), (0, 2), (1, 2)]
    print(f1(N, M, nodes, edges))

    # Test case 2:
    N = 4
    M = 4
    nodes = [(0, 0), (0, 1), (1, 0), (1, 1)]
    edges = [(0, 1), (0, 2), (1, 2), (1, 3)]
    print(f1(N, M, nodes, edges))

    # Test case 3:
    N = 5
    M = 5
    nodes = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
    print(f1(N, M, nodes, edges))


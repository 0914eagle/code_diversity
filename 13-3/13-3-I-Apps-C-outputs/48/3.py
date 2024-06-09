
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
        connected_edges = [edge for edge in edges if edge[0] == current_node or edge[1] == current_node]

        # If the current node has not been visited before, add it to the visited nodes set
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)

        # If the current node has only one edge connected to it, add the turning required for that edge
        if len(connected_edges) == 1:
            turning_required += math.pi

        # If the current node has two edges connected to it, add the turning required for both edges
        elif len(connected_edges) == 2:
            turning_required += 2 * math.pi

        # If the current node has more than two edges connected to it, return -1
        else:
            return -1

        # Get the next node to visit
        next_node = connected_edges[0][1] if connected_edges[0][0] == current_node else connected_edges[0][0]

        # If the next node has already been visited, return -1
        if next_node in visited_nodes:
            return -1

        # Add the current edge to the visited edges set
        visited_edges.add(connected_edges[0])

        # Set the current node to the next node
        current_node = next_node

    # If all nodes have been visited, return the total turning required
    if len(visited_nodes) == N:
        return turning_required

    # If not all nodes have been visited, return -1
    else:
        return -1

def f2(...):
    # Implement function 2 here
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


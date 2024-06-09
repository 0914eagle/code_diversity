
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

        # If the current node has not been visited before, add the turning required for the current node
        if current_node not in visited_nodes:
            turning_required += math.pi * 2

        # Loop through the connected edges
        for edge in connected_edges:
            # If the edge has not been visited before, add the turning required for the edge
            if edge not in visited_edges:
                turning_required += math.pi

            # Add the edge to the visited edges set
            visited_edges.add(edge)

        # Add the current node to the visited nodes set
        visited_nodes.add(current_node)

        # Set the current node to the next node
        current_node = connected_edges[0][0] if current_node == connected_edges[0][1] else connected_edges[0][1]

    # Return the total turning required
    return turning_required

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    N, M = map(int, input().split())
    nodes = []
    edges = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append((x, y))
    for i in range(M):
        x, y = map(int, input().split())
        edges.append((x, y))
    print(f1(N, M, nodes, edges))


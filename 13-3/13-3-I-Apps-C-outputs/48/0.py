
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
            turning_required += get_turning_required(connected_edges[0], nodes)

        # If the current node has two edges connected to it, add the turning required for both edges
        elif len(connected_edges) == 2:
            turning_required += get_turning_required(connected_edges[0], nodes)
            turning_required += get_turning_required(connected_edges[1], nodes)

        # If the current node has more than two edges connected to it, find the edge that is not visited before and add the turning required for that edge
        else:
            for edge in connected_edges:
                if edge not in visited_edges:
                    turning_required += get_turning_required(edge, nodes)
                    visited_edges.add(edge)
                    break

        # Find the next node to visit
        next_node = get_next_node(connected_edges, current_node)

        # If the next node is not the starting node, set it as the current node
        if next_node != 0:
            current_node = next_node

    # Return the total turning required
    return turning_required

def get_next_node(edges, current_node):
    # Find the edge that is not visited before
    for edge in edges:
        if edge[0] == current_node:
            next_node = edge[1]
        else:
            next_node = edge[0]
        if next_node not in visited_nodes:
            return next_node
    return 0

def get_turning_required(edge, nodes):
    # Get the coordinates of the two nodes connected by the edge
    node1 = nodes[edge[0]]
    node2 = nodes[edge[1]]

    # Calculate the turning required for the edge
    turning_required = math.atan2(node2[1] - node1[1], node2[0] - node1[0])

    # Return the turning required
    return turning_required

def f2(...):
    ...

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    nodes = []
    edges = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append([x, y])
    for i in range(M):
        x, y = map(int, input().split())
        edges.append([x, y])
    print(f1(N, M, nodes, edges))


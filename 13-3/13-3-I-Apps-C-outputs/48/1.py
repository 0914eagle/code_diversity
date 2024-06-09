
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

        # If the current node has not been visited before, add its turning required
        if current_node not in visited_nodes:
            turning_required += nodes[current_node][2]
            visited_nodes.add(current_node)

        # If the current node has only one edge connected to it, move to that edge
        if len(connected_edges) == 1:
            current_node = connected_edges[0][0] if connected_edges[0][1] == current_node else connected_edges[0][1]

        # If the current node has two edges connected to it, find the unvisited edge with the smallest turning required
        elif len(connected_edges) == 2:
            unvisited_edge = [edge for edge in connected_edges if edge not in visited_edges][0]
            current_node = unvisited_edge[0] if unvisited_edge[1] == current_node else unvisited_edge[1]
            visited_edges.add(unvisited_edge)

    # Add the turning required for the final edge
    turning_required += nodes[current_node][2]

    return turning_required

def f2(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    visited_edges = set()

    # Loop through all nodes
    for i in range(N):
        # Get the edges connected to the current node
        connected_edges = [edge for edge in edges if edge[0] == current_node or edge[1] == current_node]

        # If the current node has not been visited before, add its turning required
        if current_node not in visited_nodes:
            turning_required += nodes[current_node][2]
            visited_nodes.add(current_node)

        # If the current node has only one edge connected to it, move to that edge
        if len(connected_edges) == 1:
            current_node = connected_edges[0][0] if connected_edges[0][1] == current_node else connected_edges[0][1]

        # If the current node has two edges connected to it, find the unvisited edge with the smallest turning required
        elif len(connected_edges) == 2:
            unvisited_edge = [edge for edge in connected_edges if edge not in visited_edges][0]
            current_node = unvisited_edge[0] if unvisited_edge[1] == current_node else unvisited_edge[1]
            visited_edges.add(unvisited_edge)

    # Add the turning required for the final edge
    turning_required += nodes[current_node][2]

    return turning_required

if __name__ == '__main__':
    N, M = map(int, input().split())
    nodes = []
    edges = []

    for i in range(N):
        x, y, turning_required = map(int, input().split())
        nodes.append([x, y, turning_required])

    for i in range(M):
        x, y = map(int, input().split())
        edges.append([x, y])

    print(f1(N, M, nodes, edges))
    print(f2(N, M, nodes, edges))


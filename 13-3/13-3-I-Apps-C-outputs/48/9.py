
import math

def f1(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    previous_node = -1

    # Loop through the edges
    for i in range(M):
        node1, node2 = edges[i]
        if node1 not in visited_nodes:
            visited_nodes.add(node1)
            current_node = node1
        else:
            visited_nodes.add(node2)
            current_node = node2
            previous_node = node1

        # Calculate the turning required for this edge
        turning_required += calculate_turning(nodes[current_node], nodes[previous_node])

    # Calculate the turning required for the final edge
    turning_required += calculate_turning(nodes[current_node], nodes[previous_node])

    return turning_required

def f2(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    previous_node = -1

    # Loop through the edges
    for i in range(M):
        node1, node2 = edges[i]
        if node1 not in visited_nodes:
            visited_nodes.add(node1)
            current_node = node1
        else:
            visited_nodes.add(node2)
            current_node = node2
            previous_node = node1

        # Calculate the turning required for this edge
        turning_required += calculate_turning(nodes[current_node], nodes[previous_node])

    # Calculate the turning required for the final edge
    turning_required += calculate_turning(nodes[current_node], nodes[previous_node])

    return turning_required

def calculate_turning(node1, node2):
    # Calculate the angle between the two nodes
    angle = math.atan2(node2[1] - node1[1], node2[0] - node1[0])

    # Calculate the turning required for this edge
    turning_required = abs(angle)

    return turning_required

if __name__ == '__main__':
    N, M = map(int, input().split())
    nodes = []
    edges = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append((x, y))
    for i in range(M):
        node1, node2 = map(int, input().split())
        edges.append((node1, node2))
    print(f1(N, M, nodes, edges))
    print(f2(N, M, nodes, edges))


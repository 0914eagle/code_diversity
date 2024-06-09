
import math

def f1(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    previous_node = -1

    # Loop through all edges
    for i in range(M):
        node1, node2 = edges[i]
        if node1 not in visited_nodes:
            # If node1 has not been visited, add its turning required
            turning_required += nodes[node1][2]
            visited_nodes.add(node1)
            previous_node = node1
        if node2 not in visited_nodes:
            # If node2 has not been visited, add its turning required
            turning_required += nodes[node2][2]
            visited_nodes.add(node2)
            previous_node = node2

    # Add the turning required for the final edge
    turning_required += nodes[current_node][2]

    return turning_required

def f2(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited_nodes = set()
    current_node = 0
    previous_node = -1

    # Loop through all edges
    for i in range(M):
        node1, node2 = edges[i]
        if node1 not in visited_nodes:
            # If node1 has not been visited, add its turning required
            turning_required += nodes[node1][2]
            visited_nodes.add(node1)
            previous_node = node1
        if node2 not in visited_nodes:
            # If node2 has not been visited, add its turning required
            turning_required += nodes[node2][2]
            visited_nodes.add(node2)
            previous_node = node2

    # Add the turning required for the final edge
    turning_required += nodes[current_node][2]

    return turning_required

if __name__ == '__main__':
    N, M = map(int, input().split())
    nodes = []
    edges = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append([x, y, 0])
    for i in range(M):
        node1, node2 = map(int, input().split())
        edges.append([node1, node2])

    # Calculate the turning required for each node
    for i in range(N):
        node = nodes[i]
        x, y, turning_required = node
        for j in range(M):
            edge = edges[j]
            if edge[0] == i:
                node2 = nodes[edge[1]]
                x2, y2, turning_required2 = node2
                turning_required += math.atan2(y2-y, x2-x)
            elif edge[1] == i:
                node2 = nodes[edge[0]]
                x2, y2, turning_required2 = node2
                turning_required += math.atan2(y2-y, x2-x)
        nodes[i][2] = turning_required

    # Calculate the least amount of turning required for an Eulerian circuit
    turning_required = f1(N, M, nodes, edges)

    # Print the result
    print(turning_required)


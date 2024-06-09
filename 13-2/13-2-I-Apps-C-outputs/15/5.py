
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
    # Calculate the turning required for this edge
    turning = math.atan2(node2[1] - node1[1], node2[0] - node1[0])
    return turning

def main():
    # Read the input
    nodes, edges = read_input()
    # Calculate the least turning required for an Eulerian circuit
    least_turning = get_least_turning(nodes, edges)
    # Print the output
    print(least_turning)

def read_input():
    # Read the number of nodes and edges
    nodes_count, edges_count = map(int, input().split())
    # Read the nodes
    nodes = []
    for _ in range(nodes_count):
        x, y = map(int, input().split())
        nodes.append((x, y))
    # Read the edges
    edges = []
    for _ in range(edges_count):
        edge = list(map(int, input().split()))
        edges.append(edge)
    return nodes, edges

if __name__ == "__main__":
    main()


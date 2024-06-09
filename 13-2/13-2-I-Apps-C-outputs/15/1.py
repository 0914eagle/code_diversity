
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
        # If the current node has been visited before, calculate the turning required
        else:
            # Calculate the angle between the current node and the previous node
            angle = math.atan2(nodes[current_node][1] - nodes[previous_node][1], nodes[current_node][0] - nodes[previous_node][0])
            # Add the angle to the total turning
            turning += angle
        # Set the current node as the previous node for the next iteration
        previous_node = current_node
        # Set the current node as the next node
        current_node = edge

    # Calculate the total turning required for the Eulerian circuit
    total_turning = turning + math.atan2(nodes[current_node][1] - nodes[previous_node][1], nodes[current_node][0] - nodes[previous_node][0])

    return total_turning

# Test the function with the sample input
nodes = [(0, 0), (0, 1), (1, 0)]
edges = [(0, 1), (0, 2), (1, 2)]
print(get_least_turning(nodes, edges))

# Part 2: Read input from file
with open("input.txt", "r") as f:
    nodes = []
    edges = []
    for line in f:
        # Read the number of nodes and edges
        num_nodes, num_edges = map(int, line.split())
        # Read the node coordinates
        for _ in range(num_nodes):
            x, y = map(int, f.readline().split())
            nodes.append((x, y))
        # Read the edge connections
        for _ in range(num_edges):
            i, j = map(int, f.readline().split())
            edges.append((i, j))
    # Calculate the least turning required for the Eulerian circuit
    least_turning = get_least_turning(nodes, edges)
    print(least_turning)


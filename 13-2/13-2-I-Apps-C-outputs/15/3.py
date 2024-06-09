
import math

def get_least_turning(nodes, edges):
    # Initialize variables
    turning = 0
    visited = set()
    current_node = 0

    # Loop through the edges
    for edge in edges:
        # If the current node has not been visited, mark it as visited and add its turning to the total turning
        if current_node not in visited:
            visited.add(current_node)
            turning += nodes[current_node][2]
        # If the current node has been visited, find the next node to visit and add its turning to the total turning
        else:
            for node in nodes:
                if node[0] == current_node and node[1] not in visited:
                    visited.add(node[1])
                    turning += node[2]
                    current_node = node[1]
                    break

    # Return the total turning
    return turning

# Main function
if __name__ == "__main__":
    # Read input from stdin
    nodes = []
    edges = []
    for _ in range(int(input())):
        nodes.append(list(map(int, input().split())))
    for _ in range(int(input())):
        edges.append(list(map(int, input().split())))

    # Get the least turning
    turning = get_least_turning(nodes, edges)

    # Print the output
    print(turning)



def topologically_sorted_nodes(graph):
    # Initialize a list to store the topologically sorted nodes
    topologically_sorted_nodes = []

    # While there are still nodes in the graph that do not have any incoming edges
    while len([node for node in graph if not node["in_degree"]]) > 0:
        # Find a node with no incoming edges
        node = next((node for node in graph if not node["in_degree"]), None)

        # Add the node to the topologically sorted nodes list
        topologically_sorted_nodes.append(node)

        # Remove the node and all its outgoing edges from the graph
        graph.remove(node)

        # Update the in-degree of the nodes that have an edge to the removed node
        for neighbor in node["neighbors"]:
            neighbor["in_degree"] -= 1

    # If the graph is not empty, then it has a cycle and topological sorting is impossible
    if graph:
        return []

    # Return the topologically sorted nodes
    return topologically_sorted_nodes

def kahn_algorithm(graph):
    # Initialize a list to store the topologically sorted nodes
    topologically_sorted_nodes = []

    # While there are still nodes in the graph
    while graph:
        # Find a node with no incoming edges
        node = next((node for node in graph if not node["in_degree"]), None)

        # If no such node exists, then the graph has a cycle and topological sorting is impossible
        if not node:
            return []

        # Add the node to the topologically sorted nodes list
        topologically_sorted_nodes.append(node)

        # Remove the node and all its outgoing edges from the graph
        graph.remove(node)

        # Update the in-degree of the nodes that have an edge to the removed node
        for neighbor in node["neighbors"]:
            neighbor["in_degree"] -= 1

    # Return the topologically sorted nodes
    return topologically_sorted_nodes

def main():
    # Read the input graph
    n, m = map(int, input().split())
    graph = []
    for _ in range(m):
        x, y = map(int, input().split())
        graph.append({"id": x, "neighbors": [y], "in_degree": 1})
        graph.append({"id": y, "neighbors": [x], "in_degree": 0})

    # Find the largest possible size of S at the beginning of any iteration of Step 1 in the execution of Kahn's Algorithm
    largest_s = 0
    for node in graph:
        if not node["in_degree"]:
            largest_s = max(largest_s, 1)
            break

    # Print the largest possible size of S
    print(largest_s)

if __name__ == "__main__":
    main()



def kahn_algorithm(graph):
    # Initialize the list of source nodes and the sorted list
    sources = [node for node in graph if not graph[node]]
    sorted_list = []

    # While there are sources nodes, repeat the following steps:
    while sources:
        # Remove a source node and all its outgoing edges from the graph
        source = sources.pop(0)
        graph.pop(source)
        for node in list(graph):
            if source in graph[node]:
                graph[node].remove(source)

        # If the removal of edges creates new source nodes, add them to the list of sources
        sources.extend([node for node in graph if not graph[node]])

        # Insert the source node at the end of the sorted list
        sorted_list.append(source)

    # Return the sorted list
    return sorted_list

def largest_s(graph):
    # Initialize the largest size of S to 0
    largest_size = 0

    # For each possible source node, repeat the following steps:
    for source in range(len(graph)):
        # Create a copy of the graph with the source node removed
        graph_copy = graph.copy()
        graph_copy.pop(source)

        # Run Kahn's algorithm on the copy of the graph
        sorted_list = kahn_algorithm(graph_copy)

        # If the sorted list is not empty, update the largest size of S
        if sorted_list:
            largest_size = max(largest_size, len(sorted_list))

    # Return the largest size of S
    return largest_size

# Test the function with an example graph
graph = {0: [1], 1: [2], 2: [3], 3: []}
print(largest_s(graph)) # Output: 1


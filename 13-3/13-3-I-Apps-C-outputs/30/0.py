
def kahn_algorithm(graph):
    # Initialize the list of source nodes and the sorted list
    sources = [node for node in graph if not graph[node]]
    sorted_list = []

    # While there are sources to consider
    while sources:
        # Get the source node with the minimum index
        source = min(sources, key=lambda x: x[0])
        sources.remove(source)

        # Remove the source node and its outgoing edges
        graph.pop(source)
        for node in list(graph):
            if source in graph[node]:
                graph[node].remove(source)

        # If the removal of edges creates new sources, add them to the list
        sources.extend([node for node in graph if not graph[node]])

        # Insert the source node at the end of the sorted list
        sorted_list.append(source)

    # Return the sorted list
    return sorted_list

def largest_s(graph):
    # Initialize the largest size of S
    largest_s = 0

    # Iterate over all possible choices of alpha
    for alpha in range(len(graph)):
        # Clone the graph and remove the edges from alpha
        graph_clone = graph.copy()
        for node in graph_clone:
            if alpha in graph_clone[node]:
                graph_clone[node].remove(alpha)

        # Run Kahn's algorithm on the cloned graph
        sorted_list = kahn_algorithm(graph_clone)

        # Update the largest size of S
        largest_s = max(largest_s, len(sorted_list))

    # Return the largest size of S
    return largest_s

# Test the function with an example graph
graph = {0: [1], 1: [2], 2: [3], 3: []}
print(largest_s(graph))


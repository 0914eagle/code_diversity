
def topologically_sort(graph):
    # Initialize the list of source nodes
    sources = [node for node in graph if not graph[node]]
    # Initialize the sorted list
    sorted_list = []
    # Loop until there are no more sources
    while sources:
        # Get the source node with the minimum index
        source = min(sources, key=lambda x: x[0])
        # Add the source node to the sorted list
        sorted_list.append(source)
        # Remove the source node and its outgoing edges from the graph
        graph.pop(source)
        for node in list(graph):
            if source in graph[node]:
                graph[node].remove(source)
        # Update the list of sources
        sources = [node for node in graph if not graph[node]]
    return sorted_list


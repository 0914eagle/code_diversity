
def topologically_sort(graph):
    # Initialize the list of source nodes
    sources = [node for node in graph if not graph[node]]
    # Initialize the sorted list
    sorted_list = []
    # Loop until there are no more sources
    while sources:
        # Get the current source node
        current_source = sources.pop()
        # Add the current source node to the sorted list
        sorted_list.append(current_source)
        # Remove the current source node and its outgoing edges from the graph
        del graph[current_source]
        for node in list(graph):
            if current_source in graph[node]:
                graph[node].remove(current_source)
        # Add any new source nodes to the list of sources
        sources.extend([node for node in graph if not graph[node]])
    # Return the sorted list
    return sorted_list



def topologically_sort(graph):
    # Initialize the list of source nodes
    sources = [node for node in graph if not graph[node]]
    # Initialize the sorted list
    sorted_list = []
    # Loop until there are no more sources
    while sources:
        # Get the source node with the minimum index
        source = min(sources, key=lambda x: x[0])
        # Remove the source node and its outgoing edges
        sources.remove(source)
        for neighbor in graph[source]:
            # If the neighbor has no incoming edges, add it to the sources
            if neighbor not in graph:
                sources.append(neighbor)
        # Add the source node to the sorted list
        sorted_list.append(source)
    return sorted_list


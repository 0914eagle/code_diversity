
def topological_sort(n, m, edges):
    # Initialize the graph as a dictionary of adjacency lists
    graph = {i: set() for i in range(n)}
    for x, y in edges:
        graph[x].add(y)

    # Initialize the list of source nodes (nodes with no incoming edges)
    sources = [i for i in range(n) if not graph[i]]

    # Initialize the list of sorted nodes
    sorted_nodes = []

    # Loop until there are no more source nodes
    while sources:
        # Get the source node with the minimum index
        source = min(sources)
        sources.remove(source)

        # Add the source node to the list of sorted nodes
        sorted_nodes.append(source)

        # Remove the outgoing edges from the graph
        for neighbor in graph[source]:
            graph[neighbor].remove(source)
            if not graph[neighbor]:
                sources.append(neighbor)

    # Return the largest possible size of S at the beginning of Step 1
    return len(sources)

# Main function
if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        x, y = map(int, input().split())
        edges.append((x, y))
    print(topological_sort(n, m, edges))


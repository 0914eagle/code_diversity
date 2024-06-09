
def topologically_sorted_nodes(n, m, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    # Initialize a list to store the topologically sorted nodes
    topologically_sorted = []

    # Iterate through the graph until there are no more nodes to visit
    while graph:
        # Find all source nodes (nodes with no incoming edges)
        source_nodes = [node for node, edges in enumerate(graph) if not edges]

        # If there are no source nodes, the graph has at least one cycle
        if not source_nodes:
            return -1

        # Remove the source nodes and their outgoing edges from the graph
        for source_node in source_nodes:
            topologically_sorted.append(source_node)
            graph.pop(source_node)
            for edge in graph:
                if source_node in edge:
                    edge.remove(source_node)

    return len(topologically_sorted)


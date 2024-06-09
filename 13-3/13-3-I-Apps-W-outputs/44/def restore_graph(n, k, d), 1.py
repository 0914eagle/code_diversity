
def restore_graph(n, k, d):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input array d
    for i in range(n):
        # Initialize a set to store the vertices that are at most k edges away from vertex i
        reachable = set()

        # Iterate over the input array d
        for j in range(n):
            # If the distance between vertex i and vertex j is at most k, add vertex j to the set of reachable vertices
            if d[i] + d[j] <= k:
                reachable.add(j)

        # Add the set of reachable vertices to the graph dictionary with vertex i as the key
        graph[i] = reachable

    # Initialize a list to store the edges of the graph
    edges = []

    # Iterate over the graph dictionary
    for i in graph:
        # Iterate over the reachable vertices of vertex i
        for j in graph[i]:
            # If vertex j is reachable from vertex i, add the edge (i, j) to the list of edges
            if j in graph[i]:
                edges.append((i, j))

    # Return the list of edges
    return edges


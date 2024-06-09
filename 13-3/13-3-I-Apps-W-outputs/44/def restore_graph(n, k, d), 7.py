
def restore_graph(n, k, d):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Iterate over the shortest distance array d
    for i in range(n):
        # If the shortest distance is not 0, it means there is an edge between the current vertex and some other vertex
        if d[i] != 0:
            # Find the vertex that is k edges away from the current vertex
            k_away = d[i] - 1
            # Add an edge between the current vertex and the k_away vertex
            graph[i].append(k_away)
            graph[k_away].append(i)

    # Return the graph
    return graph


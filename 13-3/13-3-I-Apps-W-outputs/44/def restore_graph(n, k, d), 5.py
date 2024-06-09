
def restore_graph(n, k, d):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input array d
    for i in range(n):
        # Check if the current vertex is the starting vertex
        if d[i] == 0:
            # Add the current vertex to the graph with an empty list of neighbors
            graph[i] = []
        else:
            # Find the neighbors of the current vertex by looking at the previous vertices
            neighbors = [j for j in range(i) if d[j] == d[i] - 1]
            # Add the current vertex to the graph with its neighbors
            graph[i] = neighbors

    # Return the graph
    return graph


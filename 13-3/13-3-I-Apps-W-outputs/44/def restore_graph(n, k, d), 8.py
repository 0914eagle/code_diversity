
def restore_graph(n, k, d):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input array d
    for i in range(n):
        # If the distance is 0, it means the vertex is connected to itself
        if d[i] == 0:
            graph[i] = [i]
        # If the distance is 1, it means the vertex is connected to another vertex
        elif d[i] == 1:
            # Find the vertex that is connected to the current vertex
            for j in range(n):
                if d[j] == 1 and i != j:
                    graph[i] = [j]
                    break
        # If the distance is greater than 1, it means the vertex is connected to another vertex through a path
        else:
            # Find the vertex that is connected to the current vertex through a path
            for j in range(n):
                if d[j] == d[i] - 1 and i != j:
                    graph[i] = [j]
                    break

    # Return the graph
    return graph


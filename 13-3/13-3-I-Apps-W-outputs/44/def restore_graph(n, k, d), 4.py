
def restore_graph(n, k, d):
    # Initialize a dictionary to store the graph
    graph = {}

    # Iterate over the input array d
    for i in range(n):
        # If the distance is 0, it means the vertex is connected to itself
        if d[i] == 0:
            graph[i] = [i]
        # If the distance is 1, it means the vertex is connected to one other vertex
        elif d[i] == 1:
            # Find the vertex that is connected to the current vertex with distance 1
            for j in range(n):
                if d[j] == 1 and i != j:
                    graph[i] = [j]
                    break
        # If the distance is greater than 1, it means the vertex is connected to multiple vertices
        else:
            # Find all the vertices that are connected to the current vertex with distance 1
            connected_vertices = []
            for j in range(n):
                if d[j] == 1 and i != j:
                    connected_vertices.append(j)
            # Add the current vertex to the list of connected vertices
            connected_vertices.append(i)
            # Sort the list of connected vertices
            connected_vertices.sort()
            # Add the sorted list of connected vertices to the graph
            graph[i] = connected_vertices

    # Return the graph
    return graph


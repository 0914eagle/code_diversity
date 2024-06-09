
def number_of_paths(n, m, edges):
    # Initialize a dictionary to store the paths
    paths = {}

    # Initialize the first path to start from vertex 1
    paths[1] = [1]

    # Iterate through the edges
    for i in range(m):
        # Get the current edge
        edge = edges[i]

        # If the current edge is not a self-loop
        if edge[0] != edge[1]:
            # Get the current vertex
            vertex = edge[0]

            # If the current vertex is not already in the path
            if vertex not in paths:
                # Add the current vertex to the path
                paths[vertex] = [vertex]

            # Add the current vertex to the path
            paths[vertex].append(edge[1])

    # Initialize the number of paths to 0
    num_paths = 0

    # Iterate through the paths
    for path in paths.values():
        # If the path visits all the vertices exactly once
        if len(path) == n and len(set(path)) == n:
            # Increment the number of paths
            num_paths += 1

    # Return the number of paths
    return num_paths


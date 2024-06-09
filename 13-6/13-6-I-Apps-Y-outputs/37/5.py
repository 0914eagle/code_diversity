
def num_paths(N, M, edges):
    # Initialize a dictionary to store the paths
    paths = {}

    # Initialize the starting vertex
    start = 1

    # Iterate over the edges
    for edge in edges:
        # Get the endpoints of the edge
        a, b = edge

        # If the edge is not a self-loop
        if a != b:
            # If the starting vertex is not already in the path
            if start not in paths:
                # Add the starting vertex to the path
                paths[start] = [start]

            # If the ending vertex is not already in the path
            if b not in paths:
                # Add the ending vertex to the path
                paths[b] = [b]

            # Add the edge to the path
            paths[b].append(a)

    # Initialize a variable to store the number of paths
    num_paths = 0

    # Iterate over the paths
    for path in paths.values():
        # If the path visits all the vertices exactly once
        if len(path) == N:
            # Increment the number of paths
            num_paths += 1

    # Return the number of paths
    return num_paths


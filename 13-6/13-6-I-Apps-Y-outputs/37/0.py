
def num_paths(n, m, edges):
    # Initialize a dictionary to store the paths
    paths = {1: [1]}
    # Iterate through the edges
    for i in range(m):
        # Extract the current edge
        a, b = edges[i]
        # If the start vertex is not in the path, add it
        if a not in paths:
            paths[a] = [a]
        # If the end vertex is not in the path, add it
        if b not in paths:
            paths[b] = [b]
        # Add the current edge to the path of the start vertex
        paths[a].append(b)
        # Add the current edge to the path of the end vertex
        paths[b].append(a)
    # Initialize a set to store the visited vertices
    visited = set()
    # Initialize a variable to store the number of paths
    num_paths = 0
    # Iterate through the paths
    for path in paths.values():
        # If the path visits all the vertices exactly once, increment the number of paths
        if len(path) == n and len(set(path)) == n:
            num_paths += 1
    # Return the number of paths
    return num_paths



def number_of_paths(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the visited vertices
    visited = set()

    # Initialize a list to store the paths
    paths = []

    # Recursive function to find the paths
    def find_paths(start, path):
        # If the start vertex is the destination vertex, add the path to the list of paths
        if start == n:
            paths.append(path)
            return

        # If the start vertex has not been visited, mark it as visited and add it to the path
        if start not in visited:
            visited.add(start)
            path.append(start)

            # Recursively find the paths for all the neighbors of the start vertex
            for neighbor in neighbors[start]:
                find_paths(neighbor, path)

            # Backtrack and remove the start vertex from the path
            path.pop()
            visited.remove(start)

    # Start the recursion from vertex 1
    find_paths(1, [])

    # Return the number of paths
    return len(paths)


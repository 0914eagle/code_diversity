
def solve(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over all possible strings
    for string in itertools.product("abc", repeat=n):
        # Initialize a set to store the vertices that are connected by the current string
        connected_vertices = set()

        # Iterate over all pairs of vertices
        for i in range(n):
            for j in range(i + 1, n):
                # If the characters at the current positions in the string are equal or neighboring, add the current string to the set of possible strings
                if string[i] == string[j] or (string[i] == "a" and string[j] == "b") or (string[i] == "b" and string[j] == "c"):
                    connected_vertices.add((i + 1, j + 1))

        # If the set of connected vertices is equal to the set of edges in the graph, add the current string to the set of possible strings
        if connected_vertices == set(edges):
            strings.add("".join(string))

    # If there is exactly one possible string, return "Yes" and the string
    if len(strings) == 1:
        return "Yes\n" + list(strings)[0]

    # Otherwise, return "No"
    return "No"


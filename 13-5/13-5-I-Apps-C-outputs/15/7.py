
def find_max_independent_set(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the vertices in the independent set
    independent_set = set()

    # Iterate through the vertices and add them to the independent set if they have no neighbors in the set
    for vertex in range(1, n + 1):
        if not any(neighbor in independent_set for neighbor in neighbors[vertex]):
            independent_set.add(vertex)

    return len(independent_set)


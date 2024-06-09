
def max_independent_set(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the vertices in the maximum independent set
    max_independent_set = set()

    # Iterate through the vertices and try to add them to the independent set
    for vertex in range(1, n + 1):
        if vertex not in max_independent_set:
            # If the vertex is not already in the independent set, try to add it
            if all(neighbor not in max_independent_set for neighbor in neighbors[vertex]):
                # If the vertex has no neighbors in the independent set, add it
                max_independent_set.add(vertex)
            else:
                # If the vertex has neighbors in the independent set, try to add its neighbors instead
                for neighbor in neighbors[vertex]:
                    if neighbor not in max_independent_set:
                        max_independent_set.add(neighbor)

    return len(max_independent_set)


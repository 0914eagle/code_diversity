
def solve(n, m, edges):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Initialize a list to store the vertices that are not visited yet
    unvisited = [i for i in range(1, n + 1)]
    # Initialize a list to store the in-degrees of all vertices
    in_degrees = [0] * (n + 1)

    # Count the in-degrees of all vertices
    for edge in edges:
        in_degrees[edge[1]] += 1

    # Find the vertex with in-degree 0 and add it to the permutation
    start_vertex = unvisited[0]
    permutation[0] = start_vertex
    unvisited.remove(start_vertex)

    # Iterate through the remaining vertices
    for i in range(1, n):
        # Find the vertex with in-degree 0 and add it to the permutation
        for vertex in unvisited:
            if in_degrees[vertex] == 0:
                permutation[i] = vertex
                unvisited.remove(vertex)
                break
        # If no vertex with in-degree 0 is found, then the graph has a cycle
        else:
            return []

        # Decrement the in-degrees of all vertices that are adjacent to the current vertex
        for edge in edges:
            if edge[1] == permutation[i]:
                in_degrees[edge[0]] -= 1

    return permutation


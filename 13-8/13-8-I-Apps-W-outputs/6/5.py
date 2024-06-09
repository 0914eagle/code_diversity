
def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
        # Otherwise, calculate the number of shortest paths between the two vertices
        else:
            # Initialize a set to store the vertices that are not divisible by either v or u
            non_divisible = set()

            # Iterate over each divisor of D
            for d in range(1, D + 1):
                # If d is not divisible by either v or u, add it to the set
                if d % v != 0 and d % u != 0:
                    non_divisible.add(d)

            # Initialize a dictionary to store the number of paths from v to each vertex that is not divisible by either v or u
            paths_from_v = {}

            # Iterate over each vertex that is not divisible by either v or u
            for vertex in non_divisible:
                # Initialize a set to store the vertices that are not divisible by vertex
                non_divisible_vertices = set()

                # Iterate over each divisor of D
                for d in range(1, D + 1):
                    # If d is not divisible by vertex, add it to the set
                    if d % vertex != 0:
                        non_divisible_vertices.add(d)

                # If vertex is not divisible by either v or u, add it to the set of non-divisible vertices
                if vertex % v != 0 and vertex % u != 0:
                    non_divisible_vertices.add(vertex)

                # Calculate the number of paths from v to vertex that are not divisible by either v or u
                paths_from_v[vertex] = len(non_divisible_vertices)

            # Calculate the number of shortest paths between v and u by summing the number of paths from v to each vertex that is not divisible by either v or u
            num_paths[(v, u)] = sum(paths_from_v.values())

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] % 998244353 for v, u in queries]


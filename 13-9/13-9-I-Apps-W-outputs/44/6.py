
def solve(n, m, edges):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Initialize a list to store the in-degree of each vertex
    in_degree = [0] * n
    # Initialize a queue to store the vertices with in-degree 0
    queue = []

    # Create a dictionary to map each vertex to its adjacent vertices
    adjacency_list = {}
    for edge in edges:
        v, u = edge
        if v not in adjacency_list:
            adjacency_list[v] = []
        if u not in adjacency_list:
            adjacency_list[u] = []
        adjacency_list[v].append(u)
        in_degree[u] += 1

    # Add vertices with in-degree 0 to the queue
    for i in range(1, n+1):
        if in_degree[i-1] == 0:
            queue.append(i-1)

    # Run BFS to traverse the graph
    while queue:
        # Get the vertex with in-degree 0
        vertex = queue.pop(0)
        # Assign the next label to the vertex
        permutation[vertex] = len(permutation) - len(queue)
        # Iterate through the adjacent vertices and decrease their in-degree
        for adjacent_vertex in adjacency_list[vertex]:
            in_degree[adjacent_vertex] -= 1
            # If the in-degree of an adjacent vertex is 0, add it to the queue
            if in_degree[adjacent_vertex] == 0:
                queue.append(adjacent_vertex)

    return permutation



def get_maximum_cost(n, a, edges):
    # Initialize a dictionary to store the distances of each vertex from the root
    distances = {}
    # Initialize a variable to store the maximum cost
    max_cost = 0
    # Loop through each edge and update the distances of the vertices
    for edge in edges:
        u, v = edge
        if u not in distances:
            distances[u] = 0
        if v not in distances:
            distances[v] = 0
        distances[v] = max(distances[v], distances[u] + 1)
    # Loop through each vertex and calculate the cost of the tree
    for vertex in range(1, n + 1):
        cost = 0
        if vertex in distances:
            cost = distances[vertex] * a[vertex - 1]
        max_cost = max(max_cost, cost)
    return max_cost



def solve(n, a, edges):
    # Initialize a dictionary to store the cost of each vertex as the key, and the vertex value as the value
    costs = {i: a[i-1] for i in range(1, n+1)}

    # Iterate over the edges and update the cost of each vertex based on the distance between them
    for edge in edges:
        u, v = edge
        costs[u] += costs[v]
        costs[v] += costs[u]

    # Return the maximum cost
    return max(costs.values())


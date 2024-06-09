
def max_cost(n, a, edges):
    # Initialize a dictionary to store the cost of each vertex as the key, and the vertex label as the value
    cost = {i: a[i-1] for i in range(1, n+1)}

    # Iterate over the edges and update the cost of the vertices
    for u, v in edges:
        cost[u] += cost[v]
        cost[v] += cost[u]

    # Return the maximum cost
    return max(cost.values())


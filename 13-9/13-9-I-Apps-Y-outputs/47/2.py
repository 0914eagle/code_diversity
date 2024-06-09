
def get_maximum_cost(n, a, edges):
    # Initialize a dictionary to store the cost of each vertex as the key, and the vertex number as the value
    cost = {i: a[i-1] for i in range(1, n+1)}

    # Iterate through the edges and update the cost of the vertices
    for u, v in edges:
        cost[u] += cost[v]
        cost[v] = 0

    # Find the maximum costamoumedents = max(cost.values())
    maximum_cost = max(cost.values())

    # Return the maximum cost
    return maximum_cost


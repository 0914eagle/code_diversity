
def solve(n, a, edges):
    # Initialize a dictionary to store the distance of each vertex from the root
    dist = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and calculate the distance of each vertex from the root
    for u, v in edges:
        dist[u] = max(dist[u], dist[v] + 1)
        dist[v] = max(dist[v], dist[u] + 1)
    
    # Calculate the maximum cost of the tree
    cost = 0
    for i in range(1, n + 1):
        cost += dist[i] * a[i - 1]
    
    return cost


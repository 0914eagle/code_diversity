
def solve(n, a, edges):
    # Initialize a dictionary to store the distances from each vertex to the root
    distances = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges and update the distances
    for u, v in edges:
        distances[u] = max(distances[u], distances[v] + 1)
        distances[v] = max(distances[v], distances[u] + 1)
    
    # Calculate the maximum cost of the tree
    cost = 0
    for i in range(1, n + 1):
        cost += distances[i] * a[i - 1]
    
    return cost



def get_maximum_cost(n, a, edges):
    # Initialize a dictionary to store the distances from each vertex to the root
    distances = {}
    for i in range(n):
        distances[i+1] = 0
    
    # Iterate through the edges and update the distances
    for edge in edges:
        u, v = edge
        distances[v] = max(distances[v], distances[u] + 1)
    
    # Calculate the maximum cost by summing the distances from each vertex to the root multiplied by its value
    return sum(distances[i] * a[i-1] for i in range(1, n+1))


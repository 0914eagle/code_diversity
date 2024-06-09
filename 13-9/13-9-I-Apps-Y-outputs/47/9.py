
def get_maximum_cost(n, a, edges):
    # Initialize a dictionary to store the distance of each vertex from the root
    dist = {i: 0 for i in range(1, n + 1)}

    # Iterate through the edges and update the distance of the vertices
    for u, v in edges:
        dist[v] = dist[u] + 1
        dist[u] = dist[v] + 1

    # Calculate the maximum cost by summing the distance of each vertex from the root multiplied by its value
    return sum(dist[i] * a[i - 1] for i in range(1, n + 1))



def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {}
    for i in range(n):
        weights[i + 1] = a[i]
    
    # Initialize a dictionary to store the distances between the vertices
    distances = {}
    for i in range(n - 1):
        u, v = edges[i]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    
    # Initialize a set to store the vertices that are at a distance more than k from each other
    subset = set()
    
    # Iterate through the vertices and add them to the subset if they are at a distance more than k from each other
    for i in range(n):
        vertex = i + 1
        if vertex not in subset:
            for j in range(i + 1, n):
                neighbor = j + 1
                if neighbor not in subset and (vertex, neighbor) in distances and distances[(vertex, neighbor)] <= k:
                    break
            else:
                subset.add(vertex)
    
    # Return the maximum total weight of the subset
    return sum(weights[vertex] for vertex in subset)


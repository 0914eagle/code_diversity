
def get_maximum_weight_subset(n, k, a, edges):
    # Initialize a dictionary to store the weights of the vertices
    weights = {}
    for i in range(n):
        weights[i + 1] = a[i]
    
    # Initialize a dictionary to store the distances between vertices
    distances = {}
    for i in range(n - 1):
        u, v = edges[i]
        distances[(u, v)] = 1
        distances[(v, u)] = 1
    
    # Initialize a set to store the vertices in the maximum weight subset
    max_weight_subset = set()
    
    # Iterate through the vertices and add them to the maximum weight subset if they are valid
    for i in range(n):
        vertex = i + 1
        if vertex not in max_weight_subset:
            # Check if the vertex is valid by checking if it has a distance more than k from any other vertex in the subset
            valid = True
            for j in range(n):
                if j + 1 in max_weight_subset and (vertex, j + 1) in distances and distances[(vertex, j + 1)] <= k:
                    valid = False
                    break
            if valid:
                max_weight_subset.add(vertex)
    
    # Return the maximum weight of the subset
    return sum(weights[vertex] for vertex in max_weight_subset)


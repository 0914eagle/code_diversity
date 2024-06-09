
def solve(n, edges):
    # Find the centroid of the tree
    centroid = find_centroid(n, edges)
    
    # Cut the edge between the centroid and any other vertex
    x, y = centroid, 1
    while y in edges[x]:
        y += 1
    x_1, y_1 = x, y
    
    # Add the edge between the centroid and any other vertex
    x, y = centroid, 1
    while y in edges[x]:
        y += 1
    x_2, y_2 = x, y
    
    return x_1, y_1, x_2, y_2

def find_centroid(n, edges):
    # Initialize the centroid as the first vertex
    centroid = 1
    
    # Iterate through all vertices except the centroid
    for i in range(2, n+1):
        # If the vertex is not in the edge list of the centroid, it is a centroid
        if i not in edges[centroid]:
            centroid = i
            break
    
    return centroid


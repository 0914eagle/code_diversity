
def solve(n, edges):
    # Step 1: Find the centroid of the tree
    centroid = find_centroid(n, edges)
    
    # Step 2: Cut the edge between the centroid and any other vertex
    x, y = centroid, 1
    while y in edges[x]:
        y += 1
    return x, y

def find_centroid(n, edges):
    # Initialize the centroid as the first vertex
    centroid = 1
    
    # Iterate through all the vertices
    for i in range(2, n+1):
        # If the current vertex is not in the edge list of the centroid, it is a centroid
        if i not in edges[centroid]:
            centroid = i
            break
    
    return centroid



def find_centroid(n, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Calculate the degree of each vertex by counting the number of edges incident to it
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the vertex with the smallest degree
    min_degree = min(degrees.values())
    centroids = [vertex for vertex, degree in degrees.items() if degree == min_degree]
    
    return centroids

def solve(n, edges):
    # Find the centroid of the tree
    centroids = find_centroid(n, edges)
    
    # If there is only one centroid, return it
    if len(centroids) == 1:
        return centroids[0]
    
    # If there are multiple centroids, find the edge that connects them
    for edge in edges:
        if edge[0] in centroids and edge[1] in centroids:
            return edge
    
    # If no edge connects the centroids, return None
    return None


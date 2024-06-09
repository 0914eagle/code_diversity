
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Find the center of the hedgehog
    center = None
    for vertex, degree in degrees.items():
        if degree >= 3:
            center = vertex
            break
    
    # Check if the tree is a hedgehog
    if center is None:
        return False
    if degrees[center] < 3:
        return False
    
    # Check if the tree is a k-multihedgehog
    for vertex, degree in degrees.items():
        if vertex != center and degree != 1:
            return False
    
    return True


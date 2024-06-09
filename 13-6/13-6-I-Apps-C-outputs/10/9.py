
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
    
    # Check if the tree is a k-multihedgehog
    if center is None:
        return "No"
    if k == 1:
        return "Yes"
    
    # Create a list of vertices connected to the center
    center_neighbors = []
    for edge in edges:
        if edge[0] == center:
            center_neighbors.append(edge[1])
        elif edge[1] == center:
            center_neighbors.append(edge[0])
    
    # Check if the tree is a (k-1)-multihedgehog
    if len(center_neighbors) != k-1:
        return "No"
    for neighbor in center_neighbors:
        if degrees[neighbor] != 1:
            return "No"
    
    # Check if the tree is a k-multihedgehog
    return "Yes"


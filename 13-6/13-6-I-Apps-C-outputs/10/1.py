
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Check if the center vertex has degree at least k
    center = -1
    for i in range(1, n+1):
        if degrees[i] >= k:
            center = i
            break
    
    if center == -1:
        return "No"
    
    # Check if all other vertices have degree 1
    for i in range(1, n+1):
        if i != center and degrees[i] != 1:
            return "No"
    
    return "Yes"


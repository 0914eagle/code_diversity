
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1
    
    # Check if the degree of the center vertex is at least 3
    center = -1
    for i in range(1, n+1):
        if degrees[i] >= 3:
            center = i
            break
    
    if center == -1:
        return False
    
    # Check if the tree is a k-multihedgehog
    visited = set()
    queue = [center]
    while queue:
        vertex = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        if degrees[vertex] != 1:
            return False
        for edge in edges:
            if edge[0] == vertex or edge[1] == vertex:
                queue.append(edge[0] if edge[1] == vertex else edge[1])
    
    return True


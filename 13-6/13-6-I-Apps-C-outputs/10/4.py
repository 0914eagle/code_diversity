
def is_k_multihedgehog(n, k, edges):
    # Initialize a dictionary to store the degree of each vertex
    degrees = {}
    for i in range(1, n+1):
        degrees[i] = 0
    
    # Count the degree of each vertex based on the given edges
    for edge in edges:
        u, v = edge[0], edge[1]
        degrees[u] += 1
        degrees[v] += 1
    
    # Check if the center vertex has degree at least k
    center = -1
    for i in range(1, n+1):
        if degrees[i] >= k:
            center = i
            break
    
    # If no center vertex is found, return "No"
    if center == -1:
        return "No"
    
    # Initialize a set to store the vertices that are connected to the center vertex
    connected_vertices = set()
    for i in range(1, n+1):
        if degrees[i] == 1 and i != center:
            connected_vertices.add(i)
    
    # Check if all other vertices have degree 1
    for i in range(1, n+1):
        if i != center and degrees[i] != 1:
            return "No"
    
    # Create a list to store the hedgehogs created in each step
    hedgehogs = []
    
    # Iterate through each step and create a new hedgehog
    for step in range(k):
        # Initialize a set to store the vertices that are connected to the center vertex in the current step
        current_connected_vertices = set()
        
        # Iterate through each connected vertex and create a new hedgehog
        for vertex in connected_vertices:
            # Get the neighbor of the current vertex that is not the center vertex
            neighbor = -1
            for edge in edges:
                u, v = edge[0], edge[1]
                if u == vertex and v != center:
                    neighbor = v
                    break
            
            # Create a new hedgehog with the center vertex and the neighboring vertex
            hedgehog = [center, neighbor]
            
            # Add the hedgehog to the list of hedgehogs created in each step
            hedgehogs.append(hedgehog)
            
            # Add the neighboring vertex to the set of connected vertices in the current step
            current_connected_vertices.add(neighbor)
        
        # Set the connected vertices in the current step to the set of connected vertices in the previous step
        connected_vertices = current_connected_vertices
    
    # Check if all hedgehogs have degree at least k
    for hedgehog in hedgehogs:
        if len(hedgehog) < k:
            return "No"
    
    # If all conditions are met, return "Yes"
    return "Yes"


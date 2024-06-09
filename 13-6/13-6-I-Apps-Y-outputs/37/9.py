
def num_paths(n, m, edges):
    # Initialize a dictionary to store the number of paths for each vertex
    num_paths_dict = {1: 1}
    
    # Iterate over the edges
    for i in range(m):
        # Get the current edge
        edge = edges[i]
        
        # If the current edge is not a self-loop
        if edge[0] != edge[1]:
            # If the starting vertex of the current edge is not already in the dictionary
            if edge[0] not in num_paths_dict:
                # Add the starting vertex to the dictionary with a value of 0
                num_paths_dict[edge[0]] = 0
                
            # If the ending vertex of the current edge is not already in the dictionary
            if edge[1] not in num_paths_dict:
                # Add the ending vertex to the dictionary with a value of 0
                num_paths_dict[edge[1]] = 0
            
            # Increment the number of paths for the starting vertex
            num_paths_dict[edge[0]] += 1
            
            # Increment the number of paths for the ending vertex
            num_paths_dict[edge[1]] += 1
    
    # Initialize a variable to store the total number of paths
    total_paths = 0
    
    # Iterate over the dictionary
    for vertex, paths in num_paths_dict.items():
        # If the vertex has at least one path
        if paths > 0:
            # Increment the total number of paths
            total_paths += paths
    
    # Return the total number of paths
    return total_paths


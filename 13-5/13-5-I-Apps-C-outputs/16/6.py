
def solve(N, u, edges):
    # Initialize the longest jumping path length and number of jumping paths
    L, M = 0, 0
    
    # Initialize a dictionary to store the ancestors of each vertex
    ancestors = {i: set() for i in range(1, N+1)}
    
    # Add the root vertex as an ancestor of itself
    ancestors[1].add(1)
    
    # Iterate over the edges and update the ancestors of each vertex
    for i, j in edges:
        ancestors[j].add(i)
        ancestors[j].update(ancestors[i])
    
    # Iterate over the vertices and check if they are ancestors of the root vertex
    for i in range(2, N+1):
        # If the vertex is an ancestor of the root vertex, check if it is a valid jumping path
        if 1 in ancestors[i]:
            # Initialize the length of the jumping path and the current vertex
            length, vertex = 1, i
            
            # Iterate over the ancestors of the current vertex until the root vertex is reached
            while vertex != 1:
                # If the current vertex is not an ancestor of the root vertex, break the loop
                if 1 not in ancestors[vertex]:
                    break
                
                # If the current vertex is an ancestor of the root vertex, update the length of the jumping path
                length += 1
                
                # Update the current vertex to be the parent of the current vertex
                vertex = edges[vertex-1][0]
            
            # If the length of the jumping path is greater than the current longest jumping path, update the longest jumping path length and number of jumping paths
            if length > L:
                L, M = length, 1
            # If the length of the jumping path is equal to the current longest jumping path, update the number of jumping paths
            elif length == L:
                M += 1
    
    # Return the longest jumping path length and the number of jumping paths modulo the prime 11092019
    return L, M % 11092019


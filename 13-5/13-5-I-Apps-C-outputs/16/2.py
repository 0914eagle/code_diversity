
def solve(N, u, parent):
    # Initialize the longest jumping path length and number of jumping paths
    L, M = 0, 0
    
    # Iterate over the vertices in the tree
    for i in range(1, N+1):
        # If the current vertex is the root, skip it
        if i == 1:
            continue
        
        # Get the parent of the current vertex
        p = parent[i]
        
        # If the parent is not the root, check if the current vertex is an ancestor of the parent
        if p != 1:
            # If the current vertex is an ancestor of the parent, increment the longest jumping path length
            if u[i] >= u[p]:
                L += 1
                
                # If the current vertex is the root, increment the number of jumping paths
                if i == N:
                    M += 1
    
    # Return the longest jumping path length and the number of jumping paths modulo the prime 11092019
    return L, M % 11092019


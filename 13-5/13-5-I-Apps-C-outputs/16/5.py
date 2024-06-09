
def solve(N, u, parent):
    # Initialize the longest jumping path length and the number of jumping paths
    L, M = 0, 0
    
    # Iterate over the vertices in the tree
    for i in range(1, N+1):
        # If the current vertex is the root, skip it
        if i == 1:
            continue
        
        # Find the parent of the current vertex
        p = parent[i]
        
        # If the parent has a lower label, skip the current vertex
        if u[p] > u[i]:
            continue
        
        # If the current vertex has a higher label than the parent, update the longest jumping path length
        if u[i] > u[p]:
            L = max(L, i-p)
        
        # If the current vertex has the same label as the parent, update the number of jumping paths
        if u[i] == u[p]:
            M += 1
    
    # Return the longest jumping path length and the number of jumping paths modulo the prime 11092019
    return L, M % 11092019


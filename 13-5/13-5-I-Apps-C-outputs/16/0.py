
def solve(N, labels, parents):
    # Initialize the longest jumping path length and number of jumping paths
    L = 0
    M = 0
    
    # Iterate through the vertices of the tree
    for i in range(1, N+1):
        # If the current vertex is the root, skip it
        if i == 1:
            continue
        
        # Get the parent of the current vertex
        parent = parents[i-1]
        
        # If the parent has a label greater than the current vertex, we cannot form a jumping path
        if labels[parent-1] > labels[i-1]:
            continue
        
        # If the current vertex has a label greater than the root, we can form a jumping path
        if labels[i-1] > labels[0]:
            # Update the longest jumping path length
            L = max(L, i)
            # Increment the number of jumping paths
            M += 1
    
    # Return the longest jumping path length and the number of jumping paths modulo the prime 11092019
    return L, M % 11092019


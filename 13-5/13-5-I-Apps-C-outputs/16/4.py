
def solve(N, labels, tree):
    # Initialize variables
    L = 0
    M = 0
    
    # Iterate through the tree and find the longest jumping path
    for i in range(1, N+1):
        # If the current vertex is the root, skip it
        if i == 1:
            continue
        
        # Find the parent of the current vertex
        parent = tree[i-1]
        
        # If the parent has a lower label, skip the current vertex
        if labels[parent-1] > labels[i-1]:
            continue
        
        # If the current vertex has a higher label than the root, update L
        if labels[i-1] > labels[0]:
            L = max(L, i)
        
        # If the current vertex has a higher label than the parent, update M
        if labels[i-1] > labels[parent-1]:
            M += 1
    
    # Return the length of the longest jumping path and the number of jumping paths modulo 11092019
    return L, M % 11092019


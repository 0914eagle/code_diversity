
def solve(N, labels, tree):
    # Initialize the longest jumping path length and the number of jumping paths
    L = 0
    M = 0
    
    # Iterate over the vertices in the tree
    for v in range(1, N+1):
        # If the vertex is the root, skip it
        if v == 1:
            continue
        
        # Get the parent of the vertex
        parent = tree[v-1]
        
        # If the parent is the root, skip it
        if parent == 1:
            continue
        
        # Get the label of the vertex and its parent
        label = labels[v-1]
        parent_label = labels[parent-1]
        
        # If the label of the vertex is greater than the label of its parent, skip it
        if label > parent_label:
            continue
        
        # If the label of the vertex is equal to the label of its parent, increment the longest jumping path length
        if label == parent_label:
            L += 1
        
        # If the label of the vertex is less than the label of its parent, increment the number of jumping paths
        if label < parent_label:
            M += 1
    
    # Return the longest jumping path length and the number of jumping paths modulo the prime 11092019
    return L, M % 11092019


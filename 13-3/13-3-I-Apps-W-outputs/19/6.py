
def solve(n, k, arr):
    # Initialize a list to store the pairs of children who turn left
    pairs = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it's the first move, add them to the list of pairs
        if arr[i] != arr[i+1] and k == 1:
            pairs.append([i, i+1])
    
    # If there are no pairs, return -1
    if not pairs:
        return -1
    
    # Loop through each move
    for move in range(k-1):
        # Initialize a list to store the pairs of children who turn left in this move
        new_pairs = []
        
        # Loop through each pair of children in the current list of pairs
        for pair in pairs:
            # If the children are looking at each other, add them to the list of pairs who turn left in this move
            if arr[pair[0]] != arr[pair[1]]:
                new_pairs.append(pair)
        
        # If there are no pairs who turn left in this move, return -1
        if not new_pairs:
            return -1
        
        # Update the list of pairs to the list of pairs who turn left in this move
        pairs = new_pairs
    
    # Return the list of pairs who turn left in the final move
    return pairs



def solve(n, k, arr):
    # Initialize a list to store the pairs of children who turn left
    pairs = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it's the first move, add them to the list of pairs
        if arr[i] != arr[i+1] and len(pairs) == 0:
            pairs.append([i, i+1])
    
    # Loop through each move
    for move in range(k-1):
        # If there are no more pairs, return -1
        if not pairs:
            return -1
        
        # Initialize a list to store the pairs of children who turn left in this move
        new_pairs = []
        
        # Loop through each pair of children
        for pair in pairs:
            # If the children are looking at each other, add them to the list of pairs who turn left
            if arr[pair[0]] != arr[pair[1]]:
                new_pairs.append(pair)
        
        # Add the pairs who turn left to the list of all pairs
        pairs += new_pairs
        
        # Loop through each pair of children who turn left
        for pair in new_pairs:
            # If the children are looking at each other, turn them in the opposite direction
            if arr[pair[0]] == arr[pair[1]]:
                arr[pair[0]] = "L" if arr[pair[0]] == "R" else "R"
                arr[pair[1]] = "L" if arr[pair[1]] == "R" else "R"
    
    # Return the list of pairs of children who turn left
    return pairs


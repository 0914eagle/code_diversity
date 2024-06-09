
def solve(n, k, arr):
    # Initialize a list to store the pairs of children who will turn left
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
    for i in range(k-1):
        # Initialize a list to store the children who will turn left in this move
        turn_left = []
        
        # Loop through each pair of children
        for pair in pairs:
            # If the children are looking at each other, add them to the list of children who will turn left
            if arr[pair[0]] == arr[pair[1]]:
                turn_left.extend(pair)
        
        # Remove the pairs of children who will turn left from the list of pairs
        for child in turn_left:
            pairs.remove([child, child+1])
        
        # Add the children who will turn left to the output
        print(len(turn_left), *turn_left)
    
    # Return the final configuration
    return arr



def solve(n, k, arrangement):
    # Initialize a list to store the pairs of children who will turn left
    pairs_left = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it's the first move, add them to the list of pairs who will turn left
        if arrangement[i] != arrangement[i+1] and k == 1:
            pairs_left.append(i+1)
    
    # If there are no pairs of children who are looking at each other, return -1
    if not pairs_left:
        return -1
    
    # Loop through each move
    for move in range(k-1):
        # Initialize a list to store the pairs of children who will turn left in this move
        pairs_left_move = []
        
        # Loop through each pair of children
        for i in range(n-1):
            # If the children are looking at each other and it's not the first move, add them to the list of pairs who will turn left in this move
            if arrangement[i] != arrangement[i+1] and move > 0:
                pairs_left_move.append(i+1)
        
        # Add the pairs of children who will turn left in this move to the overall list of pairs who will turn left
        pairs_left.extend(pairs_left_move)
    
    # Return the list of pairs of children who will turn left
    return pairs_left


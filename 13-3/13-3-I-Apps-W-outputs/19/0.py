
def solve(n, k, arr):
    # Initialize a list to store the pairs of children who turn left
    pairs = []
    
    # Loop through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it's not the last pair
        if arr[i] != arr[i+1] and i < n-2:
            # Add the pair to the list of pairs
            pairs.append([i, i+1])
    
    # If there are no pairs, return -1
    if not pairs:
        return -1
    
    # Initialize a list to store the moves
    moves = []
    
    # Loop through each move
    for i in range(k):
        # Initialize a list to store the children who turn left in this move
        turn_left = []
        
        # Loop through each pair
        for pair in pairs:
            # If the children in the pair are looking at each other
            if arr[pair[0]] == arr[pair[1]]:
                # Add the children to the list of children who turn left
                turn_left.extend(pair)
        
        # Add the list of children who turn left to the list of moves
        moves.append(turn_left)
        
        # Loop through each child who turned left
        for child in turn_left:
            # If the child is looking at the left child
            if arr[child] == "L":
                # Change the child's direction to look to the right
                arr[child] = "R"
            # If the child is looking at the right child
            else:
                # Change the child's direction to look to the left
                arr[child] = "L"
    
    # Return the list of moves
    return moves


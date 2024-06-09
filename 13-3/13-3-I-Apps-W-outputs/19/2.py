
def solve(n, k, configuration):
    # Initialize a list to store the pairs of children who will turn left
    pairs_to_turn_left = []
    
    # Iterate through each pair of children
    for i in range(n-1):
        # If the children are looking at each other and it is not the last pair
        if configuration[i] != configuration[i+1] and i < n-2:
            # Add the pair to the list of pairs to turn left
            pairs_to_turn_left.append([i, i+1])
    
    # If there are no pairs to turn left, return -1
    if not pairs_to_turn_left:
        return -1
    
    # Initialize a list to store the moves
    moves = []
    
    # Iterate through each move
    for move in range(k):
        # Initialize a list to store the children who will turn left during this move
        children_to_turn_left = []
        
        # Iterate through each pair of children who will turn left
        for pair in pairs_to_turn_left:
            # If it is the last move and the pair is the last pair of children who will turn left
            if move == k-1 and pair == pairs_to_turn_left[-1]:
                # Add both children to the list of children who will turn left during this move
                children_to_turn_left.extend(pair)
            # Otherwise, add only one child to the list of children who will turn left during this move
            else:
                children_to_turn_left.append(pair[move % 2])
        
        # Add the list of children who will turn left during this move to the list of moves
        moves.append(children_to_turn_left)
    
    # Return the list of moves
    return moves


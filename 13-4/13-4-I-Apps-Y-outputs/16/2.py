
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    
    # Loop through all possible starting positions for the first piece
    for i in range(N):
        # Initialize the current position of the first piece as its starting position
        current_position = i
        
        # Initialize the number of moves made so far as 0
        moves_made = 0
        
        # Loop through all the coordinates
        for j in range(M):
            # Calculate the distance between the current position and the next coordinate
            distance = abs(X[j] - current_position)
            
            # If the distance is 0, it means we are already at the coordinate, so we don't need to move
            if distance == 0:
                continue
            
            # If the distance is 1, we can move to the next coordinate in one move
            elif distance == 1:
                current_position = X[j]
                moves_made += 1
            
            # If the distance is greater than 1, we need to move multiple times to reach the next coordinate
            else:
                # Calculate the number of moves needed to reach the next coordinate
                num_moves = distance - 1
                
                # Update the current position and the number of moves made
                current_position = X[j]
                moves_made += num_moves
        
        # If the minimum number of moves required is not yet found or if the current number of moves is less than the minimum, update the minimum
        if min_moves == float('inf') or moves_made < min_moves:
            min_moves = moves_made
    
    return min_moves


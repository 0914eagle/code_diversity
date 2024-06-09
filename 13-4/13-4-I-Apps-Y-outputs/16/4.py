
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to achieve the objective as infinity
    min_moves = float('inf')
    
    # Loop through all possible starting positions for the pieces
    for i in range(N):
        # Initialize the current position of the pieces as the ith coordinate
        current_position = X[i]
        
        # Initialize the number of moves made so far as 0
        moves_made = 0
        
        # Loop through all the coordinates to visit
        for j in range(M):
            # Calculate the distance between the current position and the next coordinate to visit
            distance = abs(current_position - X[j])
            
            # If the distance is 0, it means we are already at the coordinate, so we don't need to move
            if distance == 0:
                continue
            
            # If the distance is 1, we can move to the next coordinate in one move
            elif distance == 1:
                current_position = X[j]
                moves_made += 1
            
            # If the distance is greater than 1, we can move to the next coordinate in multiple moves
            else:
                # Calculate the number of moves required to reach the next coordinate
                num_moves = distance - 1
                
                # Add the number of moves required to the total number of moves made
                moves_made += num_moves
                
                # Set the current position to the next coordinate
                current_position = X[j]
        
        # If the total number of moves made is less than the minimum number of moves required, update the minimum number of moves required
        if moves_made < min_moves:
            min_moves = moves_made
    
    # Return the minimum number of moves required to achieve the objective
    return min_moves


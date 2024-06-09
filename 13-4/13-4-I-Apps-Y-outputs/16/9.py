
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    
    # Loop through all possible starting positions for the pieces
    for i in range(N):
        # Initialize the current position of the pieces as the ith coordinate
        current_position = X[i]
        
        # Initialize the number of moves as 0
        moves = 0
        
        # Loop through all the coordinates
        for j in range(M):
            # If the current position is not the jth coordinate, move the piece to the jth coordinate
            if current_position != X[j]:
                # Calculate the distance between the current position and the jth coordinate
                distance = abs(current_position - X[j])
                
                # Add the distance to the number of moves
                moves += distance
                
                # Update the current position to the jth coordinate
                current_position = X[j]
        
        # If the number of moves is less than the minimum number of moves, update the minimum number of moves
        if moves < min_moves:
            min_moves = moves
    
    # Return the minimum number of moves
    return min_moves


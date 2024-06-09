
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    
    # Loop through all possible starting positions for the pieces
    for i in range(N):
        # Initialize the current position of the pieces as the first coordinate
        current_position = X[i]
        
        # Initialize the number of moves to 0
        moves = 0
        
        # Loop through all the coordinates
        for j in range(M):
            # Calculate the distance between the current position and the next coordinate
            distance = abs(current_position - X[j])
            
            # If the distance is 1, move the piece to the next coordinate
            if distance == 1:
                current_position = X[j]
                moves += 1
            # If the distance is greater than 1, move the piece to the next coordinate and add the distance to the number of moves
            else:
                current_position = X[j]
                moves += distance
        
        # If the minimum number of moves is greater than the current number of moves, update the minimum number of moves
        if moves < min_moves:
            min_moves = moves
    
    # Return the minimum number of moves
    return min_moves



def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to be the total number of pieces
    min_moves = N
    
    # Iterate over all possible starting positions for the pieces
    for i in range(N):
        # Initialize the current position of the pieces as the first coordinate
        current_position = X[0]
        
        # Initialize the number of moves to be 0
        moves = 0
        
        # Iterate over all the coordinates
        for j in range(M):
            # If the current coordinate is the same as the current position of the piece, move to the next coordinate
            if X[j] == current_position:
                current_position += 1
                moves += 1
            # If the current coordinate is not the same as the current position of the piece, move the piece to that coordinate and update the current position
            else:
                current_position = X[j]
                moves += 1
        
        # If the number of moves required is less than the minimum number of moves, update the minimum number of moves
        if moves < min_moves:
            min_moves = moves
    
    # Return the minimum number of moves required to achieve the objective
    return min_moves


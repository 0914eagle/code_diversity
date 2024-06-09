
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to 0
    min_moves = 0
    
    # Loop through each coordinate
    for i in range(M):
        # If the current coordinate is not the same as the previous coordinate, we need to move the piece
        if i > 0 and X[i] != X[i-1]:
            # Increment the minimum number of moves
            min_moves += 1
        
        # If the current coordinate is not the same as the next coordinate, we need to move the piece
        if i < M-1 and X[i] != X[i+1]:
            # Increment the minimum number of moves
            min_moves += 1
    
    # Return the minimum number of moves
    return min_moves


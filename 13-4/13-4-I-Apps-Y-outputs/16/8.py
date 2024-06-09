
def solve(N, M, X):
    # Sort the coordinates in ascending order
    X.sort()
    
    # Initialize the minimum number of moves to be the number of pieces
    min_moves = N
    
    # Iterate over all possible starting points
    for i in range(N):
        # Initialize the current position to the ith coordinate
        current_position = X[i]
        
        # Initialize the number of moves to 0
        moves = 0
        
        # Iterate over all coordinates
        for j in range(M):
            # If the current position is the jth coordinate, move to the next coordinate
            if current_position == X[j]:
                current_position = X[(j + 1) % M]
                moves += 1
        
        # If the minimum number of moves is greater than the number of moves for the current starting point, update the minimum number of moves
        if moves < min_moves:
            min_moves = moves
    
    return min_moves


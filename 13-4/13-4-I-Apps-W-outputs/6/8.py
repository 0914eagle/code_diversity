
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to move from the start square to square N
    min_draws = N
    
    # Iterate over each square in the board
    for i in range(N):
        # Get the color of the current square
        color = squares[i]
        
        # If the current square is not the start square, check if the next square has the same color as the current square
        if i > 0 and squares[i+1] == color:
            # If the next square has the same color as the current square, update the minimum number of draws
            min_draws = min(min_draws, i+1)
    
    return min_draws


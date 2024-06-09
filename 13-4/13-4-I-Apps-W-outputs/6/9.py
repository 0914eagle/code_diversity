
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to move from the start square to square N
    min_draws = N
    
    # Iterate over each square in the board
    for i in range(N):
        # Get the current square color
        current_color = squares[i]
        
        # Find the index of the next square with the current color
        next_square_index = i + 1
        while next_square_index < N and squares[next_square_index] != current_color:
            next_square_index += 1
        
        # If there is a next square with the current color, update the minimum number of draws
        if next_square_index < N:
            min_draws = min(min_draws, next_square_index - i)
    
    return min_draws



def get_min_draws(N, squares):
    # Initialize the minimum number of draws to infinity
    min_draws = float('inf')
    
    # Iterate over each possible starting square
    for i in range(N):
        # Initialize the current square and the number of draws
        current_square = i
        draws = 0
        
        # Iterate over each possible color
        for color in ['Blue', 'Orange', 'Pink', 'Green', 'Red', 'Yellow']:
            # If the current square has the current color, move to the next square
            if squares[current_square] == color:
                current_square += 1
                draws += 1
                break
        
        # If the current square is the last square, update the minimum number of draws
        if current_square == N:
            min_draws = min(min_draws, draws)
    
    # Return the minimum number of draws
    return min_draws


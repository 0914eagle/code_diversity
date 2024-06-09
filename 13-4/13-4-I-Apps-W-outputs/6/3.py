
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to infinity
    min_draws = float('inf')
    
    # Iterate over each possible starting square
    for start in range(N):
        # Initialize the current square and the number of draws
        current_square = start
        draws = 0
        
        # Iterate over each possible draw
        while current_square < N:
            # Get the color of the current square
            current_color = squares[current_square]
            
            # Find the next square with the current color
            next_square = current_square + 1
            while next_square < N and squares[next_square] != current_color:
                next_square += 1
            
            # If there is no next square with the current color, break the loop
            if next_square == N:
                break
            
            # Update the current square and the number of draws
            current_square = next_square
            draws += 1
        
        # If the current square is the last square, update the minimum number of draws
        if current_square == N - 1:
            min_draws = min(min_draws, draws)
    
    # Return the minimum number of draws
    return min_draws


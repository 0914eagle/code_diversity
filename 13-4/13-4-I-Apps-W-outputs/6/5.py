
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to infinity
    min_draws = float('inf')
    
    # Loop through each possible starting square
    for start in range(N):
        # Initialize the current square and the number of draws
        current_square = start
        draws = 0
        
        # Loop through each possible draw
        for draw in range(N):
            # Get the color of the current square
            current_color = squares[current_square]
            
            # If the current square is the last square, break the loop
            if current_square == N - 1:
                break
            
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
        
        # Update the minimum number of draws if necessary
        if draws < min_draws:
            min_draws = draws
    
    # Return the minimum number of draws
    return min_draws


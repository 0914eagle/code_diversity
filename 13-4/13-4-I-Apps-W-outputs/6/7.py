
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to infinity
    min_draws = float('inf')
    
    # Loop through each possible starting square
    for i in range(N):
        # Initialize the current square and the number of draws
        current_square = i
        num_draws = 0
        
        # Loop through each possible draw
        while current_square < N:
            # Get the color of the current square
            current_color = squares[current_square]
            
            # If the current color is not the same as the previous color, increment the number of draws
            if current_color != squares[current_square - 1]:
                num_draws += 1
            
            # Move to the next square with the current color
            current_square += 1
            while current_square < N and squares[current_square] != current_color:
                current_square += 1
            
            # If we have reached the end square, break the loop
            if current_square == N:
                break
        
        # If the number of draws is less than the minimum, update the minimum
        if num_draws < min_draws:
            min_draws = num_draws
    
    # Return the minimum number of draws
    return min_draws


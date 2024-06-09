
def get_min_draws(N, squares):
    # Initialize the minimum number of draws to infinity
    min_draws = float('inf')
    
    # Loop through each possible starting square
    for i in range(N):
        # Initialize the current square and the number of draws
        current_square = i
        draws = 0
        
        # Loop through each possible color
        for color in ['Blue', 'Orange', 'Pink', 'Green', 'Red', 'Yellow']:
            # Check if the current square has the current color
            if squares[current_square] == color:
                # Move to the next square with the current color
                current_square += 1
                draws += 1
                
                # If we have reached the end square, update the minimum number of draws
                if current_square == N:
                    min_draws = min(min_draws, draws)
                    break
    
    return min_draws


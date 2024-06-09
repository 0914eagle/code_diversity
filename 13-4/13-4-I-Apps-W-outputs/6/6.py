
def solve(N, squares):
    # Initialize a dictionary to store the minimum number of draws required to reach each square
    min_draws = {1: 0}
    for i in range(2, N+1):
        # Initialize the minimum number of draws required to reach the current square to infinity
        min_draws[i] = float('inf')
    
    # Loop through each square and calculate the minimum number of draws required to reach it
    for i in range(1, N+1):
        # If the current square is not the start square, we can only move to the next square that has the same color
        if squares[i-1] != 'Start':
            # Get the color of the current square
            color = squares[i-1]
            # Loop through the previous squares and find the first square that has the same color as the current square
            for j in range(i-2, -1, -1):
                if squares[j] == color:
                    # Add 1 to the minimum number of draws required to reach the previous square
                    min_draws[i] = min(min_draws[i], min_draws[j+1] + 1)
                    break
        # If the current square is the start square, we can move to any square with the same color
        else:
            # Loop through the previous squares and find the first square that has the same color as the current square
            for j in range(i-2, -1, -1):
                if squares[j] in ['Blue', 'Orange', 'Pink', 'Green', 'Red', 'Yellow']:
                    # Add 1 to the minimum number of draws required to reach the previous square
                    min_draws[i] = min(min_draws[i], min_draws[j+1] + 1)
                    break
    
    # Return the minimum number of draws required to reach the last square
    return min_draws[N]


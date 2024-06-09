
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop over all possible starting squares
    for i in range(1, N+1):
        # Initialize the current score to 0
        score = 0
        
        # Loop over the number of moves
        for j in range(K+1):
            # Calculate the next square based on the permutation and current square
            next_square = P[i-1]
            
            # Add the cost of the current square to the score
            score += C[next_square-1]
            
            # If the next square is the same as the starting square, break the loop
            if next_square == i:
                break
            
            # Update the current square to the next square
            i = next_square
        
        # Update the maximum score if the current score is greater than the previous maximum score
        max_score = max(max_score, score)
    
    # Return the maximum score
    return max_score


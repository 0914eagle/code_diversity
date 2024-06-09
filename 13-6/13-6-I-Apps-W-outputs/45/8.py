
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop over all possible starting squares
    for i in range(1, N+1):
        # Initialize the current score to 0
        current_score = 0
        
        # Loop over the moves
        for j in range(K):
            # Calculate the next square based on the permutation
            next_square = P[i-1]
            
            # Add the cost of the current square to the current score
            current_score += C[next_square-1]
            
            # Update the maximum score if necessary
            max_score = max(max_score, current_score)
            
            # Break if the current score becomes negative
            if current_score < 0:
                break
        
    # Return the maximum score
    return max_score


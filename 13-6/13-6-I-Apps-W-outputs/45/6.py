
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each possible starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        current_score = 0
        # Loop through each possible move
        for j in range(K+1):
            # Calculate the new score after the move
            new_score = current_score + C[P[i]]
            # If the new score is greater than the maximum score, update the maximum score
            if new_score > max_score:
                max_score = new_score
            # Update the current score for the next move
            current_score = new_score
    # Return the maximum score
    return max_score


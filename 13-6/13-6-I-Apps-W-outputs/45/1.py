
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each possible starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        score = 0
        # Loop through each possible move
        for j in range(K+1):
            # Calculate the new score after the move
            score += C[P[i]]
            # Check if the new score is greater than the maximum score
            if score > max_score:
                # Update the maximum score
                max_score = score
            # Break if the piece reaches the last square
            if i == N:
                break
            # Update the current square
            i = P[i]
    # Return the maximum score
    return max_score


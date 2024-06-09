
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each possible starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        score = 0
        # Loop through each possible move
        for j in range(K+1):
            # Calculate the next square based on the permutation
            next_square = P[i]
            # Add the score of the current square to the total score
            score += C[next_square]
            # Break if we have reached the last square
            if next_square == N:
                break
            # Update the current square to the next square
            i = next_square
        # Update the maximum score if the current score is greater than the previous maximum score
        max_score = max(max_score, score)
    # Return the maximum score
    return max_score


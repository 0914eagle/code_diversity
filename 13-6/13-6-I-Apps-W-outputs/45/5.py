
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        current_score = 0
        # Loop through each move
        for j in range(K+1):
            # Calculate the next square according to the permutation
            next_square = P[i]
            # Add the cost of the next square to the current score
            current_score += C[next_square]
            # Check if the current score is greater than the maximum score
            if current_score > max_score:
                # Update the maximum score
                max_score = current_score
            # Break if we have reached the last move
            if j == K:
                break
            # Update the current square
            i = next_square
    # Return the maximum score
    return max_score


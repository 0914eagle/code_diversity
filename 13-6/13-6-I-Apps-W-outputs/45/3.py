
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        curr_score = 0
        # Loop through each move
        for j in range(K+1):
            # Calculate the next square based on the permutation
            next_square = P[i]
            # Add the cost of the current square to the current score
            curr_score += C[i]
            # If the next square is the final square, update the maximum score
            if next_square == N:
                max_score = max(max_score, curr_score)
                break
            # Update the current square and move on to the next move
            i = next_square
    # Return the maximum score
    return max_score


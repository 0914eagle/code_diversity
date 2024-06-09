
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
            # Add the score of the current square to the current score
            curr_score += C[i]
            # If the current square is the same as the starting square, break the loop
            if i == next_square:
                break
            # Update the current square to the next square
            i = next_square
        # If the current score is greater than the maximum score, update the maximum score
        if curr_score > max_score:
            max_score = curr_score
    # Return the maximum score
    return max_score


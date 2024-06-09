
def solve(N, K, P, C):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each possible starting square
    for i in range(1, N+1):
        # Initialize the current score to 0
        curr_score = 0
        # Loop through each possible move
        for j in range(K+1):
            # Calculate the next square based on the permutation and current square
            next_square = P[i-1]
            # Add the score of the current square to the current score
            curr_score += C[i-1]
            # If the next square is the same as the starting square, break the loop
            if next_square == i:
                break
            # Update the current square to the next square
            i = next_square
        # If the current score is greater than the maximum score, update the maximum score
        if curr_score > max_score:
            max_score = curr_score
    # Return the maximum score
    return max_score


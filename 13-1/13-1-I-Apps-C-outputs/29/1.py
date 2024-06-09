
def solve(N, K, board):
    # Initialize a 2D array to store the sums of the dominoes
    sums = [[0] * (N - 1) for _ in range(N - 1)]

    # Loop through each row of the board
    for i in range(N - 1):
        # Loop through each column of the board
        for j in range(N - 1):
            # Calculate the sum of the two numbers in the current position
            sums[i][j] = board[i][j] + board[i][j + 1]

    # Initialize a variable to store the maximum sum
    max_sum = 0

    # Loop through each domino
    for i in range(K):
        # Loop through each row of the board
        for j in range(N - 1):
            # Loop through each column of the board
            for k in range(N - 1):
                # Check if the current position is valid (i.e., the sum of the two numbers is non-negative)
                if sums[j][k] >= 0:
                    # Update the maximum sum if necessary
                    max_sum = max(max_sum, sums[j][k] + sums[j + 1][k] + sums[j][k + 1] + sums[j + 1][k + 1])

    # Return the maximum sum
    return max_sum


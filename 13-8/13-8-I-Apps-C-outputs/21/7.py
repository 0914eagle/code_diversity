
def solve(N, K, board):
    # Initialize a two-dimensional array to store the sums of the dominoes
    sums = [[0] * (N - 1) for _ in range(N - 1)]

    # Loop through each row of the board
    for i in range(N - 1):
        # Loop through each column of the board
        for j in range(N - 1):
            # Calculate the sum of the dominoes in the current position
            sums[i][j] = board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1]

    # Initialize a variable to store the maximum sum
    max_sum = 0

    # Loop through each possible combination of dominoes
    for i in range(K):
        for j in range(K):
            # Calculate the sum of the current combination of dominoes
            current_sum = sums[i][j] + sums[i + 1][j + 1]

            # Update the maximum sum if the current sum is greater than the previous maximum sum
            if current_sum > max_sum:
                max_sum = current_sum

    # Return the maximum sum
    return max_sum


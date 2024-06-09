
def solve(N, K, board):
    # Initialize a two-dimensional array to store the sums of the numbers in each row
    sums = [[0] * 3 for _ in range(N)]

    # Calculate the sum of the numbers in each row
    for i in range(N):
        for j in range(3):
            sums[i][j] = sums[i][j - 1] + board[i][j]

    # Initialize a variable to store the maximum sum
    max_sum = 0

    # Iterate through all possible combinations of dominoes
    for i in range(K):
        for j in range(i, K):
            # Calculate the sum of the numbers covered by the current combination of dominoes
            sum = 0
            for k in range(N):
                sum += max(sums[k][j], sums[k][i]) - sums[k][i - 1]

            # Update the maximum sum if necessary
            if sum > max_sum:
                max_sum = sum

    return max_sum


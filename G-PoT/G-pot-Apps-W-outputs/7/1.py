
# Define a function to calculate the minimum expected number of turns
def min_expected_turns(board):
    n = 10
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(1, i+1):
            dp[i] = min(dp[i], dp[i-j] + 1)

    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                dp[board[i][j]] = min(dp[board[i][j]], dp[i])

    return dp[-1]

# Read input board
board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

# Calculate and print the minimum expected number of turns
result = min_expected_turns(board)
print(result)

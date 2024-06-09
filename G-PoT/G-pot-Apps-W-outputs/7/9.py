
# Read input
board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

# Initialize variables
dp = [[0.0] * 10 for _ in range(10)]
dp[0][0] = 0.0

# Calculate expected number of turns
for i in range(10):
    for j in range(10):
        if (i, j) == (0, 0):
            continue
        total_prob = 0.0
        for k in range(1, 7):
            ni, nj = i, j + k
            if ni >= 10:
                ni = 9 - (ni - 9)
            if nj >= 10:
                nj = 9 - (nj - 9)
            if board[ni][nj] != 0:
                ni = board[ni][nj]
            total_prob += min(dp[ni][nj], dp[i][j] + 1)
        dp[i][j] = total_prob / 6.0

# Output result
print("{:.10f}".format(dp[9][0]))

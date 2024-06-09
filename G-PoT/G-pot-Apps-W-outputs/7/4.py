
import numpy as np

def expected_turns(board):
    n = 10
    dp = np.zeros((n, n))
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                dp[i][j] = dp[board[i][j]][j]
            else:
                for k in range(1, 7):
                    next_i = i
                    next_j = j + k
                    if next_j >= n:
                        next_i -= 1
                        next_j = n - 1 - (next_j - n)
                    dp[i][j] += min(dp[next_i][next_j], dp[board[next_i][next_j]][next_j]) + 1
                dp[i][j] /= 6
    return dp[0][0]

board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

result = expected_turns(board)
print("{:.10f}".format(result))

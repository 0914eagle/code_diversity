
import numpy as np

def calculate_expected_turns(board):
    n = 10
    dp = np.zeros((n, n))
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] == 0:
                dp[i][j] = 1 + np.mean([dp[min(i+h, n-1)][j] for h in range(1, 7)])
            else:
                dp[i][j] = dp[board[i][j]][j]
    return dp[0][0]

board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

result = calculate_expected_turns(board)
print("{:.10f}".format(result))

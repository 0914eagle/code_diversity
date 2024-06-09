
import numpy as np

def calculate_expected_turns(board):
    n = 10
    dp = np.zeros((n, n))
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] > 0:
                dp[i][j] = dp[board[i][j]][j]
            else:
                min_turns = float('inf')
                for k in range(1, 7):
                    ni = i
                    nj = j + k
                    if nj >= n:
                        ni -= 1
                        nj = n - 1 - (nj - n)
                    min_turns = min(min_turns, 1 + dp[ni][nj])
                dp[i][j] = min_turns
    return dp[0][0]

board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

expected_turns = calculate_expected_turns(board)
print(expected_turns)

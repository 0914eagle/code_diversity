
import numpy as np

def min_expected_turns(board):
    n = len(board)
    dp = np.zeros((n, n))
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                dp[i][j] = 1 + dp[board[i][j]][j]
            else:
                min_turns = float('inf')
                for k in range(1, 7):
                    next_i = i + k
                    next_j = j
                    if next_i >= n:
                        next_i = n - 1
                        next_j = 10 - (next_i - i)
                    min_turns = min(min_turns, 1 + dp[next_i][next_j])
                dp[i][j] = min_turns
    
    return dp[0][0]

# Input
board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

# Output
result = min_expected_turns(board)
print(result)

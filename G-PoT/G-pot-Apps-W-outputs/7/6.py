
import numpy as np

def solve_game(board):
    n = 10
    dp = np.zeros((n, n))
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] == 0:
                dp[i][j] = 1 + np.mean([dp[min(i+r, n-1)][j] for r in range(1, 7)])
            else:
                dp[i][j] = dp[board[i][j]][j]
    
    return dp[0][0]

# Input
board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

# Output
result = solve_game(board)
print("{:.10f}".format(result))

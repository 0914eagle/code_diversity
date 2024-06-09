
import numpy as np

# Read input
board = []
for _ in range(10):
    row = list(map(int, input().split()))
    board.append(row)

# Initialize probabilities array
probabilities = np.zeros((10, 10))
probabilities[9][0] = 1

# Calculate minimum expected number of turns
for i in range(9, -1, -1):
    for j in range(10):
        if board[i][j] != 0:
            probabilities[board[i][j]][j] += probabilities[i][j]
        else:
            for k in range(1, 7):
                next_i = i - k
                next_j = j
                if next_i < 0:
                    next_i = 0
                    next_j = j + 1
                if next_j > 9:
                    next_j = 9
                probabilities[next_i][next_j] += probabilities[i][j] / 6

# Output the result
print("{:.10f}".format(np.sum(probabilities)))

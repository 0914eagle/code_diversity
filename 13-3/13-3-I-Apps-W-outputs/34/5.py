
import sys

def solve(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[c[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not a digit, skip it
            if A[i][j] == -1:
                continue

            # If the current cell is a digit, loop through its neighbors
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is a digit and has a higher value, update the dp table
                    if A[k][l] != -1 and A[k][l] > A[i][j]:
                        dp[i][j] = min(dp[i][j], dp[k][l] + c[A[i][j]])

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

H, W = map(int, input().split())
c = [int(x) for x in input().split()]
A = [list(map(int, input().split())) for _ in range(H)]
print(solve(H, W, c, A))


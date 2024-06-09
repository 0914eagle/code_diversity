
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

            # If the current cell is the last row or column, set the cost to 0
            if i == H-1 or j == W-1:
                dp[i][j] = 0
                continue

            # Find the minimum cost of turning the current digit into 1
            dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + c[A[i][j]]

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[0][j] for j in range(W))

if __name__ == '__main__':
    H, W = map(int, input().split())
    c = [int(x) for x in input().split()]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(solve(H, W, c, A))



import sys

def solve(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[float('inf') for _ in range(10)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                dp[i][A[i][j]] = c[A[i][j]]

    # Fill in the dp table using the recurrence relation
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                for k in range(10):
                    if k != A[i][j]:
                        dp[i][k] = min(dp[i][k], dp[i][A[i][j]] + c[A[i][j]])

    # Return the minimum total cost to turn all digits into 1
    return min(dp[i][1] for i in range(H))

if __name__ == '__main__':
    H, W = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(solve(H, W, c, A))


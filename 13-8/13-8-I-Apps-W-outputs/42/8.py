
import sys

def solve(r1, c1, r2, c2):
    # Initialize a 2D array to store the values of f(i, j)
    dp = [[0] * (c2+1) for _ in range(r2+1)]

    # Base case: f(i, j) = 1 when i == 0 or j == 0
    for i in range(r2+1):
        dp[i][0] = 1
    for j in range(c2+1):
        dp[0][j] = 1

    # Fill in the 2D array using the recurrence relation
    for i in range(1, r2+1):
        for j in range(1, c2+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # Return the sum modulo 10^9+7
    return sum(dp[r2][c2]) % (10**9+7)

if __name__ == '__main__':
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    print(solve(r1, c1, r2, c2))



import sys

def solve(n, m, p):
    # Initialize the dp array with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column
        for j in range(1, m + 1):
            # If the current cell is not blocked by an obstacle
            if dp[i][j] == 0:
                # Check if the current cell is in the last row
                if i == n:
                    # If it is, set the number of ways to place obstacles to 1
                    dp[i][j] = 1
                else:
                    # Otherwise, add the number of ways to place obstacles in the next row
                    dp[i][j] += dp[i + 1][j]

                # Check if the current cell is in the last column
                if j == m:
                    # If it is, add the number of ways to place obstacles in the previous row
                    dp[i][j] += dp[i - 1][j]
                else:
                    # Otherwise, add the number of ways to place obstacles in the next column
                    dp[i][j] += dp[i][j + 1]

    # Return the number of ways to place obstacles modulo p
    return dp[1][1] % p

n, m, p = map(int, sys.stdin.readline().split())
print(solve(n, m, p))


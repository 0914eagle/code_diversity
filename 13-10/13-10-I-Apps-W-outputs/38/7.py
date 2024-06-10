
import sys

def count_ways(n, k):
    # Initialize a 2D array to store the results
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: if k is 0, there is only one way to place rooks
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    return dp[n][k]

def main():
    n, k = map(int, sys.stdin.readline().split())
    print(count_ways(n, k) % 998244353)

if __name__ == '__main__':
    main()


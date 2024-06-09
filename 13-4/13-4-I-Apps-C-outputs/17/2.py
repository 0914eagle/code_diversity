
import sys

def count_ways(n, m, conditions):
    # Initialize a 2D array to store the number of ways to paint each square
    dp = [[0] * (n + 1) for _ in range(3)]
    dp[0][0] = 1

    # Loop through each condition
    for i in range(m):
        l, r, x = conditions[i]
        for j in range(l - 1, r):
            for k in range(3):
                dp[k][j + 1] += dp[k][j]
            dp[0][j + 1] -= dp[0][j]
        dp[0][r] = 0

    # Return the number of ways to paint the last square
    return dp[0][n] % 1000000007

def main():
    n, m = map(int, input().split())
    conditions = []
    for _ in range(m):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(count_ways(n, m, conditions))

if __name__ == '__main__':
    main()



import sys

def count_ways(N, M, conditions):
    # Initialize a 2D array to store the number of ways to paint each square
    dp = [[0] * (N + 1) for _ in range(3)]
    dp[0][0] = 1

    # Iterate over the conditions
    for i in range(M):
        l, r, x = conditions[i]
        for j in range(l, r + 1):
            for k in range(3):
                dp[k][j] += dp[(k + 1) % 3][j - 1]
            dp[0][j] += dp[1][j - 1] + dp[2][j - 1]

    # Return the number of ways to paint the last square
    return dp[0][N] % 1000000007

def main():
    N, M = map(int, input().split())
    conditions = []
    for i in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(count_ways(N, M, conditions))

if __name__ == '__main__':
    main()


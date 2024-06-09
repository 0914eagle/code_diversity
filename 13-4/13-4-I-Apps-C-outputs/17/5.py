
import sys

def get_input():
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    return N, M, conditions

def count_ways(N, M, conditions):
    # Initialize the dp table with the number of ways to paint each square
    dp = [1, 1, 1] + [0] * (N - 1)
    for l, r, x in conditions:
        for i in range(l, r + 1):
            dp[i] = (dp[i - 1] + dp[i] + dp[i + 1]) % 1000000007
    return dp[N]

def main():
    N, M, conditions = get_input()
    print(count_ways(N, M, conditions))

if __name__ == '__main__':
    main()


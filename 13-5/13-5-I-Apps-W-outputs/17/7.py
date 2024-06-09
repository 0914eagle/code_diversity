
import itertools
import sys

def solve(s, p, subsequence):
    n = len(s)
    m = len(subsequence)
    if m == 0:
        return 1
    if m == 1:
        return 1 if s[subsequence[0] - 1] == p[0] else 0
    if s[subsequence[0] - 1] != p[0]:
        return 0
    if subsequence[0] + len(p) - 1 == n:
        return 1 if s[subsequence[0] - 1:subsequence[0] + len(p) - 1] == p else 0
    dp = [0] * (n - m + 2)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(subsequence[i - 1], n + 1):
            if j == subsequence[i - 1]:
                dp[j] += dp[j - 1]
            elif j > subsequence[i - 1] and s[j - 1] == p[i - 1]:
                dp[j] += dp[j - 1]
    return dp[n]

def main():
    n, m = map(int, input().split())
    p = input()
    subsequence = list(map(int, input().split()))
    print(solve(input()[:n], p, subsequence) % 1000000007)

if __name__ == '__main__':
    main()


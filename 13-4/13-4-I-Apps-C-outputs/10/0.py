
import sys

def solve(S):
    n = len(S)
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if S[j] != S[i - 1]:
                dp[i] = (dp[i] + dp[j]) % mod
    return dp[n]

if __name__ == '__main__':
    sys.stdin = open('input.txt')
    while True:
        N = int(input())
        S = input().strip()
        if N == 0 and S == '':
            break
        print(solve(S))


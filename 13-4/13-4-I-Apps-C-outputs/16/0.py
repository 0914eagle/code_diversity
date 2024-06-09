
def longest_interesting_subsequence(A, S):
    N = len(A)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
        if dp[i] > S:
            return i - 1
    return N

N, S = map(int, input().split())
A = list(map(int, input().split()))
print(*[longest_interesting_subsequence(A[i:], S) for i in range(N)], sep='\n')


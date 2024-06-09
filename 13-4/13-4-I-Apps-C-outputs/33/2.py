
def f1(N, M, ps):
    # Calculate the probability of Anthony winning the game
    p = 0
    for i in range(N+M-1):
        p += ps[i] * (1 - ps[i]) ** (N+M-2-i)
    return p

def f2(N, M, ps):
    # Calculate the probability of Anthony winning the game using dynamic programming
    dp = [0] * (N+M)
    dp[0] = 1
    for i in range(1, N+M):
        for j in range(i):
            dp[i] += ps[j] * dp[i-j-1]
    return dp[N+M-1]

if __name__ == '__main__':
    N, M = map(int, input().split())
    ps = [float(input()) for _ in range(N+M-1)]
    print(f1(N, M, ps))
    print(f2(N, M, ps))


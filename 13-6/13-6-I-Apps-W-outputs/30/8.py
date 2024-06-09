
def get_max_sum(a, m):
    n = len(a)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = a[i - 1] % j
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1] % j)
    return dp[n][m]

def solve(n, m, a):
    return get_max_sum(a, m)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, m, a))



def max_m(a, k):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(n):
        dp[0][i] = a[i]
    for i in range(1, k + 1):
        for j in range(i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1])
        for j in range(i, n):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
    return max(dp[k])

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(max_m(a, k))

if __name__ == '__main__':
    main()


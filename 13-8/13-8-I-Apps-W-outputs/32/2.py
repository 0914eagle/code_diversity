
def get_max_comfort(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + (a[i - 1] ^ a[j - 1]))
    return dp[n][n]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_comfort(a))

if __name__ == '__main__':
    main()


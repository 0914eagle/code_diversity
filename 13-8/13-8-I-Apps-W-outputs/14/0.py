
def min_steps(a, b):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]

def main():
    n = int(input())
    a = [0] * n
    b = [int(x) for x in input().split()]
    print(min_steps(a, b))

if __name__ == '__main__':
    main()


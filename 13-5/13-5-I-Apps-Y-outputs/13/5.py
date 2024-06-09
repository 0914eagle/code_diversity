
def f1(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for x in range(i):
                    dp[i][j] = min(dp[i][j], dp[x][j-1] + n-x)
    return dp[n][k]

def f2(s, k):
    n = len(s)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for x in range(i):
                    dp[i][j] = min(dp[i][j], dp[x][j-1] + n-x)
    return dp[n][k]

if __name__ == '__main__':
    s = input()
    k = int(input())
    print(f1(s, k))
    print(f2(s, k))


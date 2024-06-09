
def get_max_score(a, l, r):
    return sum(a[l:r+1])

def get_min_score(a, l, r):
    return -sum(a[l:r+1])

def solve(a):
    n = len(a)
    dp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][i] = get_max_score(a, i-1, i-1)
    for i in range(n-1):
        for j in range(i+1, n+1):
            dp[i][j] = max(dp[i][k] + get_min_score(a, k+1, j-1) for k in range(i, j))
    return dp[0][-1]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))



def solve(a):
    n = len(a)
    dp = [-1] * n
    for i in range(n):
        if a[i] % 2 == 0:
            dp[i] = 1
        else:
            for j in range(i+1, min(n, i+a[i]+1)):
                if a[j] % 2 == 1:
                    dp[i] = 2
                    break
            for j in range(max(0, i-a[i]), i):
                if a[j] % 2 == 1:
                    dp[i] = 2
                    break
    return dp


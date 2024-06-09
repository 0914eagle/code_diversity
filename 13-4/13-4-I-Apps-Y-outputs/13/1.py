
def get_monotonic_renumerations(arr):
    n = len(arr)
    dp = [1] * (n + 1)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            dp[i] = dp[i - 1]
        dp[i] += dp[i - 1]
    return dp[n]

def solve(n, arr):
    renumerations = get_monotonic_renumerations(arr)
    return renumerations % 998244353

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))


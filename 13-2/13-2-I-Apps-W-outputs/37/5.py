
import math

def get_coprime_subsequences(arr):
    n = len(arr)
    dp = [1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if arr[i - 1] % arr[j - 1] == 0:
                dp[i] = (dp[i] + dp[j - 1]) % (10**9 + 7)
    return dp[n]

arr = list(map(int, input().split()))
print(get_coprime_subsequences(arr))


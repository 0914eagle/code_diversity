
import math

def get_coprime_subsequences(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if math.gcd(arr[i - 1], arr[j]) == 1:
                dp[i] += dp[j]
        dp[i] = dp[i] % (10**9 + 7)
    return dp[n]

n = int(input())
arr = list(map(int, input().split()))
print(get_coprime_subsequences(arr))


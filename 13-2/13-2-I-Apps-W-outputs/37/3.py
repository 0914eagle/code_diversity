
import math

def get_coprime_subsequences(a):
    n = len(a)
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i):
            if a[i - 1] % a[j - 1] == 0:
                dp[i] = (dp[i] - dp[j] + 1000000007) % 1000000007
    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(get_coprime_subsequences(a))



from math import isqrt

def count_distinct_prime_factors(num):
    count = 0
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
            count += 1
    if num > 1:
        count += 1
    return count

def max_revenue(N, data):
    dp = [0] * (1 << N)
    for mask in range(1, 1 << N):
        for i in range(N):
            if mask & (1 << i):
                new_mask = mask ^ (1 << i)
                dp[mask] = max(dp[mask], dp[new_mask] + count_distinct_prime_factors(data[i]))
    return dp[(1 << N) - 1]

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    print(max_revenue(N, data))
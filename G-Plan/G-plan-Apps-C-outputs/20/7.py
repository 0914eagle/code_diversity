
from math import isqrt

def count_prime_factors(num):
    factors = set()
    while num % 2 == 0:
        factors.add(2)
        num //= 2
    for i in range(3, isqrt(num) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 2:
        factors.add(num)
    return len(factors)

def max_revenue(N, data):
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for mask in range(1 << N):
            for j in range(N):
                if mask & (1 << j) == 0:
                    dp[i][mask | (1 << j)] = max(dp[i][mask | (1 << j)], dp[i - 1][mask] + count_prime_factors(data[j]))
    
    return dp[N][(1 << N) - 1]

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    print(max_revenue(N, data))

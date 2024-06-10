t_prime_factors(num):
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return len(factors)

def max_revenue(N, data):
    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for mask in range(1 << N):
            for j in range(N):
                if mask & (1 << j) == 0:
                    new_mask = mask | (1 << j)
                    dp[i][new_mask] = max(dp[i][new_mask], dp[i - 1][mask] + count_prime_factors(data[j]))
    return dp[N][(1 << N) - 1]

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    print(max_revenue(N, data))

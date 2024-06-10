revenue(N, data):
    def prime_factors_count(num):
        count = 0
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                count += 1
                while num % i == 0:
                    num //= i
        if num > 1:
            count += 1
        return count

    dp = [[0] * (1 << N) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1 << N):
            for k in range(N):
                if j & (1 << k) == 0:
                    dp[i][j | (1 << k)] = max(dp[i][j | (1 << k)], dp[i - 1][j] + prime_factors_count(data[k]))

    return dp[N][(1 << N) - 1]

if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    print(max_revenue(N, data))

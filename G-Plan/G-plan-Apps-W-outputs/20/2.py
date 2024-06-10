
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    dp = [0] * (1 << n)
    dp[0] = 1

    for mask in range(1, 1 << n):
        valid = True
        for i in range(n):
            if mask & (1 << i):
                for j in range(i + 1, n):
                    if mask & (1 << j) and (int(T[i], 2) & int(T[j], 2)) == 0:
                        valid = False
                        break
                if not valid:
                    break

        if valid:
            dp[mask] = 1
            for i in range(n):
                if mask & (1 << i):
                    dp[mask] = (dp[mask] * dp[mask ^ (1 << i)]) % MOD

    total_good_sets = 0
    for mask in range(1, 1 << n):
        if mask & (1 << n - 1):
            total_good_sets = (total_good_sets + dp[mask]) % MOD

    return total_good_sets

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)


MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    dp = [0] * (1 << n)
    dp[0] = 1

    for mask in range(1 << n):
        valid = True
        for i in range(n):
            if (mask & (1 << i)) > 0:
                for j in range(i + 1, n):
                    if (mask & (1 << j)) > 0 and (int(T[i], 2) & int(T[j], 2)) == 0:
                        valid = False
                        break
                if not valid:
                    break

        if valid:
            subset = 0
            for i in range(n):
                if (mask & (1 << i)) > 0:
                    subset |= int(T[i], 2)
            if subset <= M:
                dp[mask] = sum(dp[mask ^ (1 << i)] for i in range(n)) % MOD

    return sum(dp) % MOD

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

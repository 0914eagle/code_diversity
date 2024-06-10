
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    bitmask_dp = [0] * (1 << n)
    bitmask_dp[0] = 1

    for mask in range(1, 1 << n):
        valid = True
        for i in range(n):
            if (mask >> i) & 1:
                for j in range(i + 1, n):
                    if (mask >> j) & 1:
                        if (int(T[i], 2) & int(T[j], 2)) != int(T[i], 2):
                            valid = False
                            break
                if not valid:
                    break

        if valid:
            bitmask_dp[mask] = 1

    dp = [0] * (1 << n)
    dp[0] = 1

    for mask in range(1, 1 << n):
        for submask in range(mask, 0, -1):
            if bitmask_dp[submask]:
                dp[mask] = (dp[mask] + dp[mask ^ submask]) % MOD

    total_good_sets = 0
    for mask in range(1, 1 << n):
        if bitmask_dp[mask]:
            total_good_sets = (total_good_sets + dp[(1 << n) - 1 - mask]) % MOD

    return total_good_sets

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

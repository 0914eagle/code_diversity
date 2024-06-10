
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    valid_sets = 0
    bitmask_dp = [0] * (1 << n)
    bitmask_dp[0] = 1

    for i in range(1, 1 << n):
        bits = bin(i).count('1')
        bitmask = 0
        for j in range(n):
            if i & (1 << j):
                bitmask |= int(T[j], 2)
        if bitmask <= M and bits == bin(bitmask).count('1'):
            bitmask_dp[i] = 1

    for i in range(1, 1 << n):
        if bitmask_dp[i]:
            for j in range(n):
                if i & (1 << j) == 0 and (i | (1 << j)) < (1 << n):
                    bitmask_dp[i | (1 << j)] = (bitmask_dp[i | (1 << j)] + bitmask_dp[i]) % MOD

    for i in range(1, 1 << n):
        valid_sets = (valid_sets + bitmask_dp[i]) % MOD

    return valid_sets

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

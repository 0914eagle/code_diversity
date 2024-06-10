
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    dp = [0] * (1 << n)
    dp[0] = 1

    for i in range(1, 1 << n):
        valid = True
        for j in range(n):
            if i & (1 << j):
                for k in range(j + 1, n):
                    if i & (1 << k):
                        if int(T[j], 2) & int(T[k], 2) == 0:
                            valid = False
                            break
                if not valid:
                    break

        if valid:
            dp[i] = 1

    for i in range(1 << n):
        for j in range(n):
            if i & (1 << j) == 0:
                dp[i | (1 << j)] = (dp[i | (1 << j)] + dp[i]) % MOD

    total_good_sets = sum(dp) % MOD
    return total_good_sets

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

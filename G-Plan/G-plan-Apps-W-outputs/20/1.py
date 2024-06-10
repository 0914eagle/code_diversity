
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    valid_sets = 0
    for i in range(1, 1 << n):
        bitmask = i
        valid = True
        for j in range(n):
            if bitmask & (1 << j):
                for k in range(j + 1, n):
                    if bitmask & (1 << k):
                        if int(T[j], 2) & int(T[k], 2) > M:
                            valid = False
                            break
                if not valid:
                    break
        if valid:
            valid_sets += 1
    return valid_sets % MOD

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

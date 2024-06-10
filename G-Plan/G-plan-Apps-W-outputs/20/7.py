
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    valid_sets = 0
    for bitmask in range(1 << n):
        subset = set()
        for i in range(n):
            if bitmask & (1 << i):
                subset.add(int(T[i], 2))
        
        if all(x in subset for x in subset) and all(x & y in subset for x in subset for y in subset) and all(x <= M for x in subset):
            valid_sets += 1
    
    return valid_sets % MOD

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

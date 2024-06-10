
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    valid_sets = 0
    for mask in range(1, 1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(int(T[i], 2))
        
        is_good = True
        for a in subset:
            if a > M:
                is_good = False
                break
            for b in subset:
                if a & b not in subset:
                    is_good = False
                    break
            if not is_good:
                break
        
        if is_good:
            valid_sets += 1
    
    return valid_sets % MOD

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

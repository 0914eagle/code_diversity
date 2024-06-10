
MOD = 10**9 + 7

def count_good_sets(m, n, T):
    M = 2**m - 1
    elements = [int(binary, 2) for binary in T]
    elements_set = set(elements)
    
    dp = [0] * (1 << n)
    dp[0] = 1
    
    for mask in range(1, 1 << n):
        valid = True
        for i in range(n):
            if mask & (1 << i):
                for j in range(i + 1, n):
                    if mask & (1 << j):
                        if (elements[i] & elements[j]) not in elements_set:
                            valid = False
                            break
                if not valid:
                    break
        
        if valid:
            dp[mask] = 1
            for i in range(n):
                if mask & (1 << i):
                    dp[mask] = (dp[mask] * dp[mask ^ (1 << i)]) % MOD
    
    total_good_sets = sum(dp) % MOD
    return total_good_sets

if __name__ == "__main__":
    m, n = map(int, input().split())
    T = [input().strip() for _ in range(n)]
    result = count_good_sets(m, n, T)
    print(result)

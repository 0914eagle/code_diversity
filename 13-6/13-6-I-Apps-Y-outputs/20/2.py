
def get_max_copies(s, k):
    n = len(s)
    if k > n:
        return []
    
    counts = [0] * (n + 1)
    for i in range(n):
        counts[s[i]] += 1
    
    t = [0] * k
    for i in range(k):
        max_count = 0
        for j in range(1, n+1):
            if counts[j] > max_count:
                max_count = counts[j]
                t[i] = j
        counts[t[i]] -= 1
    
    return t


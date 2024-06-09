
def solve(s, k):
    n = len(s)
    if k > n:
        return []
    
    count = [0] * (n + 1)
    for i in range(n):
        count[i + 1] = count[i] + 1
        if s[i] != s[i - 1]:
            count[i + 1] = max(count[i + 1], count[i])
    
    result = []
    for i in range(n, k - 1, -1):
        if count[i] > count[i - 1]:
            result.append(s[i - 1])
            count[i - 1] = count[i]
    
    return result[::-1]


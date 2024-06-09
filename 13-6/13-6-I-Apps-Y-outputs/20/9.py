
def get_max_copies(s, k):
    n = len(s)
    if k > n:
        return []
    
    count = [0] * (n + 1)
    for i in range(n):
        count[i + 1] = count[i]
        if s[i] == s[i - 1]:
            count[i + 1] += 1
    
    max_copies = 0
    result = []
    for i in range(n - k + 1):
        if count[i + k] - count[i] > max_copies:
            max_copies = count[i + k] - count[i]
            result = s[i:i+k]
    
    return result


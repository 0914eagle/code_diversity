
def get_max_distance(s):
    n = len(s)
    max_diff = 0
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(i-j)
            if s[i] != s[j] and diff > max_diff:
                max_diff = diff
    return max_diff


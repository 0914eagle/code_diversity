
def is_sorted_by_swaps(s):
    n = len(s)
    for i in range(n):
        if s[i] != 'a' and s[i] != 'b':
            return "NO"
    for i in range(n-1):
        if s[i] > s[i+1]:
            return "NO"
    return "YES"


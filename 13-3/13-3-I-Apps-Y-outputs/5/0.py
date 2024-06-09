
def is_sorted_coloring(s):
    n = len(s)
    if n == 1:
        return "YES"
    if n == 2:
        if s[0] == s[1]:
            return "NO"
        else:
            return "YES"
    if s[0] > s[1]:
        return "NO"
    for i in range(2, n):
        if s[i] < s[i-1] and s[i] < s[i-2]:
            return "NO"
    return "YES"


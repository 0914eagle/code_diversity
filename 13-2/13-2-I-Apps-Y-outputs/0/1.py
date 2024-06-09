
def is_sorted_string(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] > s[j]:
                return "NO"
    return "YES"


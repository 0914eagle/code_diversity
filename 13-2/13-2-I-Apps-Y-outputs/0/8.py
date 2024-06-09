
def is_sorted_string(s):
    n = len(s)
    if n == 1:
        return "YES"
    else:
        for i in range(n-1):
            if s[i] > s[i+1]:
                return "NO"
        return "YES"

